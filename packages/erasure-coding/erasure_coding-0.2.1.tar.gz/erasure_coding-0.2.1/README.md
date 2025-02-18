# py-erasure-coding

Bindings for the [RUST Erasure Coding](https://github.com/paritytech/erasure-coding) maintained by Parity Technologies.

This library provides a simple erasure coding API and way to commit to the resulting erasure coded data using Binary Merkle Tree.


## Installation

### Compile for local development

```
pip install -r requirements.txt
maturin develop
```
### Build wheels
```
pip install -r requirements.txt

# Build local OS wheel
maturin build --release

# Build manylinux1 wheel
docker run --rm -v $(pwd):/io ghcr.io/pyo3/maturin build --release

```
