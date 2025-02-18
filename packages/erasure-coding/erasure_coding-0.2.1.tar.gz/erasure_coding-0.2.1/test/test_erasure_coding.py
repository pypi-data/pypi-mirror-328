import json
import os
import unittest
from os import path
from random import sample

from parameterized import parameterized
from erasure_coding import (create_segments_from_data, reconstruct_data_from_segments, segment_root_for_data,
                            create_chunks_from_data, create_ec_from_data, reconstruct_data_from_ec, erasure_root,
                            create_page_proofs_from_data)


def get_test_vectors(file_filter=None):
    test_vectors = []
    abs_dir = path.join(path.dirname(path.abspath(__file__)), 'vectors')
    for filename in os.listdir(str(abs_dir)):
        if filename.endswith('.json'):
            if file_filter is None or filename.startswith(file_filter):
                with open(path.join(abs_dir, filename)) as f:

                    if file_filter:
                        filename = filename.replace(file_filter, '')

                    test_vectors.append((filename.replace('.json', ''), json.load(f)))

    return test_vectors


class TestErasureCoding(unittest.TestCase):

    @parameterized.expand(get_test_vectors(file_filter='ec_'))
    def test_ec(self, name, test_vector):
        original_data = bytes.fromhex(test_vector['data'])
        generated_chunks = create_ec_from_data(bytes.fromhex(test_vector['data']))

        # chunks = [(idx, bytes.fromhex(c)) for idx, c in enumerate(test_vector['chunks'])]
        chunks = [bytes.fromhex(c) for c in test_vector['chunks']]

        self.assertListEqual(chunks[:len(chunks)], generated_chunks[:len(chunks)])

        recovered_data = reconstruct_data_from_ec(chunks, len(original_data))

        self.assertEqual(original_data, recovered_data)

    @parameterized.expand(get_test_vectors(file_filter='page_proof'))
    def test_page_proof(self, name, test_vector):
        original_data = bytes.fromhex(test_vector['data'])

        (page_proofs, segment_root) = create_page_proofs_from_data(original_data)

        page_proofs = [bytes(p).hex() for p in page_proofs]
        segment_root = bytes(segment_root).hex()

        self.assertEqual(test_vector['page_proofs'], page_proofs)
        self.assertEqual(test_vector['segments_root'], segment_root)

    @parameterized.expand(get_test_vectors(file_filter='segment_ec'))
    def test_segment_ec(self, name, test_vector):

        original_data = bytes.fromhex(test_vector['data'])

        segments_raw = create_segments_from_data(original_data)
        segments = [[(idx, bytes(chunk)) for idx, chunk in segment] for segment in segments_raw]
        serialized_segments = [{"segment_ec": [chunk.hex() for _, chunk in segment]} for segment in segments]

        self.assertEqual(test_vector['segments'], serialized_segments)

        # Reconstruct data with 342 random chunks
        if len(segments) > 0:
            segments[0] = sample(segments[0], 342)

        recovered_data = bytes(reconstruct_data_from_segments(segments, len(original_data)))

        self.assertEqual(original_data, recovered_data)

    @parameterized.expand(get_test_vectors(file_filter='segment_root'))
    def test_segment_root(self, name, test_vector):
        original_data = bytes.fromhex(test_vector['data'])

        generated_chunks = create_chunks_from_data(bytes.fromhex(test_vector['data']), 1023)

        segment_root = segment_root_for_data(original_data, len(generated_chunks[0]))

        self.assertEqual(test_vector['chunks_root'], segment_root.hex())


if __name__ == '__main__':
    unittest.main()
