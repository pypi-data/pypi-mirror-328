use pyo3::prelude::*;

use pyo3::types::{PyBytes};
use ::erasure_coding::{ChunkIndex, construct_chunks, MerklizedChunks, Segment, SEGMENT_SIZE, SubShardDecoder, SubShardEncoder, IncompleteSegments, PageProof};
use ::erasure_coding::segment_proof::{MerklizedSegments, PageProofIndex, MAX_SEGMENT_PROOF_LEN, PAGE_PROOF_SEGMENT_HASHES};
use ::erasure_coding::segment_proof::PAGE_PROOF_SEGMENT_HASHES_SIZE;
use pyo3::exceptions::PyValueError;

fn create_chunks_from_data_inner(data: Vec<u8>, n_chunks: u16) -> Vec<Vec<u8>> {
	// let mut encoder = SubShardEncoder::new().unwrap();

	construct_chunks(n_chunks, &data).unwrap()
}

#[pyfunction]
fn create_chunks_from_data(data: Vec<u8>, n_chunks: u16, py: Python) -> PyResult<Vec<Py<PyBytes>>> {

	let chunks = create_chunks_from_data_inner(data, n_chunks);

	// Convert each Vec<u8> in chunks to PyBytes
    let py_chunks: Vec<Py<PyBytes>> = chunks.into_iter()
        .map(|chunk| PyBytes::new(py, &chunk[..]).into())
        .collect();

	Ok(py_chunks.into())
}

// #[pyfunction]
// fn recover_data_from_chunks(chunks: Vec<(u16, Vec<u8>)>, n_chunks: u16, data_len: usize, py: Python) -> PyResult<Py<PyBytes>> {
//
// 	// Convert Python list of tuples to Vec<(ChunkIndex, Vec<u8>)>
//     let chunks: Vec<(ChunkIndex, Vec<u8>)> = chunks.into_iter()
//         .map(|item| {
//             let (index, data) = item;
//             (ChunkIndex::from(index), data)
//         })
//         .collect();
//
// 	let threshold = recovery_threshold(n_chunks).unwrap();
//
// 	if  threshold > chunks.len() as u16 {
// 		return Err(PyValueError::new_err(format!("At least {} chunks required to recover data", threshold)))
// 	}
//
// 	let reconstructed: Vec<u8> = reconstruct(n_chunks, chunks, data_len).unwrap();
// 	Ok(PyBytes::new(py, &reconstructed[..]).into())
// }

// #[pyfunction]
// fn reconstruct_data_from_chunks(chunks: Vec<Vec<u8>>, py: Python) -> PyResult<Py<PyBytes>> {
// 	// Convert segment_ec data back to bytes and prepare subshards
// 		let mut subshards: Vec<(u8, ChunkIndex, SubShard)> = Vec::new();
// 		let mut chunk_idx= 0;
// 		for chunk_bytes in chunks {
// 			if chunk_idx >= 684 {
// 				let mut subshard = [0u8; SUBSHARD_SIZE];
// 				subshard[..chunk_bytes.len()].copy_from_slice(&chunk_bytes);
// 				subshards.push((1, ChunkIndex(chunk_idx as u16), subshard));
// 			}
// 			chunk_idx += 1;
// 		}
//
// 		// Initialize decoder, call reconstruct!
// 		let mut decoder = SubShardDecoder::new().unwrap();
// 		let (reconstructed_segments, _nb_decode) = decoder
// 			.reconstruct(&mut subshards.iter().map(|(s_idx, c_idx, subshard)| {
// 				(*s_idx, *c_idx, subshard as &SubShard)
// 			}))
// 			.unwrap();
//
// 		// Check the result
// 		// assert_eq!(reconstructed_segments.len(), 1);
// 		// let original_data_bytes = hex::decode(&json_data.data).expect("Failed to decode hex string");
// 		// // Verify that the data attribute matches the first 342 bytes of the reconstructed data in the first segment
// 		// if let Some((_, first_segment)) = reconstructed_segments.get(0) {
// 		// 	assert_eq!(&first_segment.data[..342], &original_data_bytes[..342], "The first 342 bytes of the reconstructed data do not match the original data.");
// 		// 	println!("Reconstructed successfully! YAY");
// 		// } else {
// 		// 	panic!("No reconstructed segments found.");
// 		// }
// 		if let Some((_, first_segment)) = reconstructed_segments.get(0) {
// 			Ok(PyBytes::new(py, &first_segment[..]).into())
// 		} else {
// 			Err(PyValueError::new_err(format!("Invalid secret_key")))
// 		}
// }

fn root_build(data: &[u8], chunk_len: usize) -> MerklizedChunks {
	let chunks_for_root: Vec<_> = data.chunks(chunk_len).map(|s| s.to_vec()).collect();

	// chunks root
	let iter = MerklizedChunks::compute(chunks_for_root.clone());
	let chunks_root: [u8; 32] = iter.root().into();

	// chunks root with segment proof code
	let proof = MerklizedSegments::compute(
		chunks_for_root.len(),
		true,
		false,
		chunks_for_root.iter().map(|i| &i[..]),
	);
	assert_eq!(chunks_root, proof.root());
	iter
}

fn segment_root_for_data_inner(data: Vec<u8>, chunk_len: usize) -> [u8; 32] {
	// let mut chunks: Vec<Vec<u8>> = Vec::new();
	// for chunk in construct_chunks(N_CHUNKS * 3, &data).unwrap() {
	// 	chunks.push(chunk);
	// }
	let merlized = root_build(data.as_slice(), chunk_len);
	merlized.root().into()
}

#[pyfunction]
fn segment_root_for_data(data: Vec<u8>, chunk_len: usize, py: Python) -> PyResult<Py<PyBytes>> {
	// let mut chunks: Vec<Vec<u8>> = Vec::new();
	// for chunk in construct_chunks(N_CHUNKS * 3, &data).unwrap() {
	// 	chunks.push(chunk);
	// }
	let data: [u8; 32] = segment_root_for_data_inner(data, chunk_len);
	Ok(PyBytes::new(py, &data).into())
}

#[pyfunction]
fn erasure_root(chunks: Vec<Vec<u8>>, py: Python) -> PyResult<Py<PyBytes>> {
	let root = MerklizedChunks::compute(chunks).root();
	let data: [u8; 32] = root.into();
	Ok(PyBytes::new(py, &data).into())
}

struct Array<const OS: usize>([u8; OS]);

impl<const OS: usize> Default for Array<OS> {
	fn default() -> Self {
		Self([0u8; OS])
	}
}

impl<const OS: usize> AsRef<[u8; OS]> for Array<OS> {
	fn as_ref(&self) -> &[u8; OS] {
		&self.0
	}
}

#[pyfunction]
fn create_ec_from_data(data: Vec<u8>, py: Python) -> PyResult<Vec<Py<PyBytes>>> {
	let chunk_result = create_ec_from_data_inner(data);

	match chunk_result {
		Ok(chunks) => {
			let py_chunks: Vec<Py<PyBytes>> = chunks
				.into_iter()
				.map(|chunk| PyBytes::new(py, &chunk).into()) // Convert Vec<u8> to PyBytes
				.collect();

			Ok(py_chunks)
		},
		Err(err_msg) => Err(PyValueError::new_err(err_msg))
	}
}


fn create_ec_from_data_inner(data: Vec<u8>) -> Result<Vec<Vec<u8>>, &'static str> {
	let package_size = data.len();

	match package_size {
		1 => Ok(create_ec_from_data_internal::<1, 2>(data)),
		684 => Ok(create_ec_from_data_internal::<684, 2>(data)),
		1368 => Ok(create_ec_from_data_internal::<{ 684 * 2 }, { 2 * 2 }>(data)),
		2052 => Ok(create_ec_from_data_internal::<{ 684 * 3 }, { 2 * 3 }>(data)),
		4096 => Ok(create_ec_from_data_internal::<4096, { 2 * 6 }>(data)),
		4104 => Ok(create_ec_from_data_internal::<{ 684 * 6 }, { 2 * 6 }>(data)),
		_ => Err("Undefined EC size"),
	}
}

fn create_ec_from_data_internal<const S: usize, const OS: usize>(data: Vec<u8>) -> Vec<Vec<u8>> {
	let mut input = [0u8; S];
	input.copy_from_slice(&data);

	let mut encoder = SubShardEncoder::new().unwrap();
	let mut chunks: Vec<Vec<u8>> = Vec::new();

	for shard in
		encoder.construct_subshards::<S, OS, _>(&[Array(input)]).unwrap()[0].into_iter()
	{
		chunks.push(Vec::from(shard));
	}

	chunks
}

#[pyfunction]
fn reconstruct_data_from_ec(chunks: Vec<Vec<u8>>, package_size: usize, py: Python) -> PyResult<Py<PyBytes>> {
	let recover_result = reconstruct_data_from_ec_inner(chunks, package_size);

	match recover_result {
		Ok(data) => {
			Ok(PyBytes::new(py, &data).into())
		},
		Err(err_msg) => Err(PyValueError::new_err(err_msg))
	}
}

fn reconstruct_data_from_ec_inner(chunks: Vec<Vec<u8>>, package_size: usize) -> Result<Vec<u8>, &'static str> {

	match package_size {
		1 => Ok(reconstruct_data_from_ec_internal::<1, 2>(chunks)),
		684 => Ok(reconstruct_data_from_ec_internal::<684, 2>(chunks)),
		1368 => Ok(reconstruct_data_from_ec_internal::<{ 684 * 2 }, { 2 * 2 }>(chunks)),
		2052 => Ok(reconstruct_data_from_ec_internal::<{ 684 * 3 }, { 2 * 3 }>(chunks)),
		4096 => Ok(reconstruct_data_from_ec_internal::<4096, { 2 * 6 }>(chunks)),
		4104 => Ok(reconstruct_data_from_ec_internal::<{ 684 * 6 }, { 2 * 6 }>(chunks)),
		_ => Err("Undefined EC size"),
	}
}

fn reconstruct_data_from_ec_internal<const S: usize, const OS: usize>(chunks: Vec<Vec<u8>>) -> Vec<u8> {
	let mut decoder = SubShardDecoder::new().unwrap();
	let r:(Vec<(u8, Box<[u8; S]>)>, usize) = decoder
		.reconstruct_subshards(
			&mut chunks
				.iter()
				.enumerate()
				// subsets
				.map(|(i, c)| {
					let mut se = [0u8; OS];
					se.copy_from_slice(c);

					(0, ChunkIndex(i as u16), se)
				}),
		)
		.unwrap();
	let mut data:Vec<u8> = Vec::new();
	// Ok(data)
	data.extend_from_slice(&r.0[0].1[..]);
	data
}

fn build_segments(data: &[u8]) -> Vec<Segment> {
	data.chunks(SEGMENT_SIZE)
		.map(|s| {
			let mut se = [0u8; SEGMENT_SIZE];
			se[0..s.len()].copy_from_slice(s);
			Segment { data: Box::new(se) }
		})
		.collect()
}

fn create_segments_from_data_inner(data: Vec<u8>) -> Vec<Vec<(u16, [u8; 12])>> {
	let segments_chunks = build_segments(&data);
	let mut encoder = SubShardEncoder::new().unwrap();
	let mut segments: Vec<Vec<(u16, [u8; 12])>> = Vec::new();
	for segment_chunks in encoder.construct_chunks(&segments_chunks).unwrap().into_iter() {
		let mut segment = Vec::with_capacity(segment_chunks.len());
		for (idx, chunk) in segment_chunks.iter().enumerate() {
			segment.push((idx as u16, *chunk));
		}
		segments.push(segment);
	}
	segments
}

#[pyfunction]
fn create_segments_from_data(data: Vec<u8>) -> Vec<Vec<(u16, [u8; 12])>> {

	create_segments_from_data_inner(data)
}

fn reconstruct_data_from_segments_inner(segments: Vec<Vec<(u16, [u8; 12])>>, data_length: usize) -> Vec<u8> {
	let mut decoder = SubShardDecoder::new().unwrap();
	let mut data:Vec<u8> = Vec::new();
	// not running segments in parallel (could be but simpler code here)
	for (seg_index, segment) in segments.iter().enumerate() {
		let r = decoder
			.reconstruct(
				&mut segment
					.iter()
					.map(|&c| (seg_index as u8, ChunkIndex(c.0 as u16), c.1)),
			)
			.unwrap();
		assert_eq!(r.1, 1);
		assert_eq!(r.0.len(), 1);
		assert_eq!(r.0[0].0, seg_index as u8);

		data.extend_from_slice(&*r.0[0].1)
		// assert_eq!(r.0[0].1, segments_chunks[seg_index].data);
	}
	data[..data_length].to_vec()
}

#[pyfunction]
fn reconstruct_data_from_segments(segments: Vec<Vec<(u16, [u8; 12])>>, data_length: usize) -> Vec<u8> {
	reconstruct_data_from_segments_inner(segments, data_length)
}

fn build_page_proofs(data: &[u8]) -> Vec<(usize, Box<[u8; PAGE_PROOF_SEGMENT_HASHES_SIZE]>)> {
	data.chunks(PAGE_PROOF_SEGMENT_HASHES_SIZE)
		.map(|s| {
			let mut se = [0u8; PAGE_PROOF_SEGMENT_HASHES_SIZE];
			se[0..s.len()].copy_from_slice(s);
			(s.len() / 32, Box::new(se))
		})
		.collect()
}

fn create_page_proofs_from_data_inner(data: Vec<u8>) -> (Vec<Vec<u8>>, Vec<u8>) {
	let nb_hash = std::cmp::min(2048, data.len() / 32);
	let data = &data[..nb_hash * 32];

	let page_proofs = build_page_proofs(&data);

	// then build a exported segment root from it.
	let segment_proof = MerklizedSegments::compute(
		nb_hash,
		true,
		true,
		data.chunks(32).take(nb_hash),
	);

	let mut check_build = IncompleteSegments::new(segment_proof.root());
	let nb_page = page_proofs.len() as u16;
	let mut proof_buf: [&[u8]; MAX_SEGMENT_PROOF_LEN] = Default::default();

	let mut encoded_page_proofs: Vec<Vec<u8>> = Vec::with_capacity(nb_page as usize);

	for (i, (nb_hash, page)) in page_proofs.iter().enumerate() {
		// we bound subtree to less than 64 only, otherwise
		// this is part of a proof larger than a page that is aligned
		// to next power of two so we have to use all tree depth even
		// if it is a single hash.
		let bound = if nb_page == 1 { *nb_hash } else { PAGE_PROOF_SEGMENT_HASHES };
		let subtree_root = MerklizedSegments::compute(
			bound,
			true,
			true,
			page.chunks(32).take(bound),
		);

		assert!(segment_proof.contains_hash(subtree_root.root()));

		let mut encoded_page = [0u8; 4096];
		encoded_page[0..2048].copy_from_slice(&page[..]);
		let page_proof_index = PageProofIndex(i as u16);
		let proof = segment_proof.page_proof_proof(&mut proof_buf, page_proof_index);
		let mut enc_at = 2048;
		for p in proof {
			encoded_page[enc_at..enc_at + 32].copy_from_slice(p);
			enc_at += 32;
		}
		let pp = PageProof { index: page_proof_index, parent_proof: &segment_proof };
		let mut other = [0u8; 4096];
		pp.encoded(&mut other);
		assert_eq!(&encoded_page, &other);
		assert_eq!(
			check_build.insert_page_proof_hashes(&encoded_page, page_proof_index),
			Some(true)
		);
		assert!(segment_proof.check_page_proof_root(
			&mut proof_buf,
			page_proof_index,
			subtree_root.root()
		));

		encoded_page_proofs.push(encoded_page.to_vec());
	}
	assert_eq!(check_build.nb_page_proof(), nb_page);

	// into.segments_root[..].copy_from_slice(segment_proof.root());

	(encoded_page_proofs, segment_proof.root().to_vec())
}


#[pyfunction]
fn create_page_proofs_from_data(data: Vec<u8>) -> (Vec<Vec<u8>>, Vec<u8>) {
	create_page_proofs_from_data_inner(data)
}

/// A Python module implemented in Rust.
#[pymodule]
fn erasure_coding(m: &Bound<'_, PyModule>) -> PyResult<()> {
    m.add_function(wrap_pyfunction!(create_ec_from_data, m)?)?;
    m.add_function(wrap_pyfunction!(reconstruct_data_from_ec, m)?)?;
    m.add_function(wrap_pyfunction!(create_chunks_from_data, m)?)?;
    m.add_function(wrap_pyfunction!(create_segments_from_data, m)?)?;
    m.add_function(wrap_pyfunction!(reconstruct_data_from_segments, m)?)?;
    m.add_function(wrap_pyfunction!(erasure_root, m)?)?;
    m.add_function(wrap_pyfunction!(segment_root_for_data, m)?)?;
    m.add_function(wrap_pyfunction!(create_page_proofs_from_data, m)?)?;
    Ok(())
}
#[cfg(test)]
mod tests {
    use super::*;
    use std::{fs::File, io::Read};
    use lazy_static::lazy_static;

    use serde::{Deserialize, Serialize};
    use serde_json;
	use ::erasure_coding::{ChunkIndex, SubShard, SUBSHARD_SIZE, SubShardDecoder};

	#[derive(Serialize, Deserialize, Debug)]
    struct JsonData {
        data: String,
        segment: SegmentData,
    }

    #[derive(Serialize, Deserialize, Debug)]
    struct SegmentData {
        segments: Vec<Segment>,
    }

    #[derive(Serialize, Deserialize, Debug)]
    struct Segment {
        segment_ec: Vec<String>,
    }

    // lazy_static! {
    //     static ref RING_DATA: Vec<u8> = {
    //         let manifest_dir = std::env::var("CARGO_MANIFEST_DIR").expect("CARGO_MANIFEST_DIR is not set");
    //         let filename = format!("{}/data/zcash-srs-2-11-uncompressed.bin", manifest_dir);
    //         let mut file = File::open(filename).expect("Failed to open SRS file");
    //         let mut ring_data = Vec::new();
    //         file.read_to_end(&mut ring_data).expect("Failed to read SRS file");
    //         ring_data
    //     };
    // }
	#[test]
    fn test_segments() {
		let data =  hex::decode("9f5721d79f73e36244d5b6741d46f1f966b4a5b28261f199579ef06cdaaeeda99f6942f3fe32d4d1d115ad523adb2d99c3ff0e7f43b145fd22b817ed9c71f4996b1715c921a536401b0e0f883f650cc4d33d1a39aead41444666549a44ce9b00a566cf660d24e4c68df683c39d1a5687ae9a9ffe58c9cb75b4bc66b31b3b74cdb3f95e1044c1369f930ba148bc68d7a01ab2c5f8eb793ac984abeb5466df080000df66b8f616b7a6629ffe347070f26e9e8c1030447b6c06fa147b754a51c58b226aebaa3318cc6168c17335977bd56949978a6e5f2297c9d0892c6a3a220936a2e1302255ec61b74f3b5d35bff779eecec580d72081f21977954d469819c2149fbab48ffa2d0668651e8c885a14cc6fa75e684ae834d329241a21400b4c3e6bf6d1155120c9d2f237f9f9c30e49c8a908a97655848f4dfc5ccc041f8b13a34dc8c3016376e55bc9b29fb56ab5c15102c551ffe03c3143677c3d31acf0cc6e3595e6ae80e6fe0fdfa6e6d97c55e9e1f3cc579dd35264dfe8dcdde83a9ef35b8e3e1e3cf01aaa9284fb193aa163426e3c15cb018802e37dc846b0b997e8ec9fefa302e38667c39547b7d73673b3793419272e2150d0a32b091b7c0284033f82ca5499987e2ba8647ed45c5f2dee338e208d96ff86924a78d1b958b21462e8ca2b0162d7eea6df2a905d24ffb048fc791379086ca22625cc3be452ab88323578935f08d61e7c373e01e4fccd25c3e660563e347d9b415c2faedc766d9110448134262745e8bf9898b8d4dd2c9120cf462fbfdb2405e418e05a699ddf45cbf97219f528bd0cde3dfbede136b6633683f14022ffaabc35488bbff444cc7e0cd99f38478a105aa61db02930dbe0217fe56b2f54c8d4094a0e56ab2b13c8d19c8c62290855bb07fc08a33ad943e9a43c404ccbaa72fd80dd4d2edb4abdb6b3bbae313cea2d4b1078218a61bf391c6a").unwrap();
		// let segments = create_segments_from_data_inner(data.clone());
		let segments = create_segments_from_data_inner(data.clone());


		let reconstructed_data = reconstruct_data_from_segments_inner(segments, data.len());
		assert_eq!(&data, &reconstructed_data);

	}

	#[test]
    fn test_ec_from_data() {
		let data =  hex::decode("2f").unwrap();
		// let chunks = create_chunks_from_data_inner(data.clone());
		// let chunks2 = create_chunks_from_data_inner(data);
		let chunks = create_ec_from_data_inner(data.clone()).unwrap();
		let recovered_data = reconstruct_data_from_ec_inner(chunks, data.len()).unwrap();
		assert_eq!(&data, &recovered_data);
	}

	#[test]
	fn test_page_proof_from_data() {
		let data = hex::decode("").unwrap();
		let page_proofs = create_page_proofs_from_data_inner(data);
		assert_eq!(page_proofs.0.len(), 0);

		let data = hex::decode("6c6cc0b4447c7893582ef0f58ce86e39e3879a39f9bf131e74912ea2b9cfe810").unwrap();
		let page_proofs = create_page_proofs_from_data_inner(data);
		assert_eq!(page_proofs.0[0], hex::decode("6c6cc0b4447c7893582ef0f58ce86e39e3879a39f9bf131e74912ea2b9cfe8100000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000").unwrap());
		assert_eq!(page_proofs.1, hex::decode("6c6cc0b4447c7893582ef0f58ce86e39e3879a39f9bf131e74912ea2b9cfe810").unwrap());
	}
}
