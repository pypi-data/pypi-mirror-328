# CITEgeist: Cellular Indexing of Transcriptomes and Epitopes for Guided Exploration of Intrinsic Spatial Trends

CITEgeist is a computational method for deconvolving spatial transcriptomics data using spatially-resolved CITE-seq measurements. The pipeline performs both cell-type proportion estimation and gene expression deconvolution in a two-pass approach, leveraging both protein and RNA measurements from the same spatial locations.

## Quick Installation

You can now also install CITEgeist using pip:

```bash
pip install citegeist
```

## Table of Contents
1. [System Requirements](#system-requirements)
    - [Software Dependencies](#software-dependencies)
    - [Hardware Requirements](#hardware-requirements)
2. [Getting Started](#getting-started)
    - [1. Installation](#1-installation)
    - [2. Set Up the Environment](#2-set-up-the-environment)
    - [3. Obtain Gurobi License](#3-obtain-gurobi-license)
    - [4. Running CITEgeist](#4-running-citegeist)
3. [Benchmarking and Reproducibility](#benchmarking-and-reproducibility)
4. [Run the Analysis](#run-the-analysis)

## System Requirements

### Software Dependencies

- **Operating System**:  
  - Linux  
  - macOS  
  - Windows 10 with WSL2  

- **Python**: 3.10
- **Gurobi** [version > 3.9](https://www.gurobi.com/downloads/gurobi-software/)
#### Key Python Dependencies
- scanpy==1.10.4
- anndata==0.11.3
- numpy==1.26.4
- pandas==2.2.3
- scipy==1.13.1
- scikit-learn==1.6.1
- gurobipy==11.0.2 (requires license)
- matplotlib==3.10.0
- seaborn==0.13.2
- h5py==3.12.1
- squidpy==1.6.2
- spatialdata==0.2.5.post0

It is recommended to install the dependencies in the `CITEgeist_env.yml` file for running the notebooks.

### Hardware Requirements
- **RAM**: Minimum 16GB, Recommended 64GB+
- **Storage**: 16GB minimum for installation and basic analysis
- **CPU**: Multi-core processor recommended (8+ cores for optimal performance)

---

## Getting Started

### 1. Installation

Install CITEgeist using pip:

```bash
pip install citegeist
```

For development installation:

```bash
git clone https://github.com/acc383/CITEgeist.git
cd CITEgeist
pip install -e .[dev]
```

### 2. Set Up the Environment

- Create and activate a new conda environment:

```bash
conda create -n citegeist python=3.10
conda activate citegeist
```

### 3. Obtain Gurobi License

CITEgeist requires a Gurobi license (free for academic use):

1. Sign up for an academic license at: [https://www.gurobi.com/downloads/end-user-license-agreement-academic/](https://www.gurobi.com/downloads/end-user-license-agreement-academic/)
2. Follow the instructions to download and install your license.
3. Update the license file path in your code to match your local license location.

### 4. Running CITEgeist

You can run CITEgeist in two ways:

#### A. Using Python Scripts
- Expected runtime on a standard computer (16 threads, 32GB RAM):
  - Small dataset: ~2 hours
  - Medium dataset: ~4 hours
  - Large dataset: ~10 hours

#### Key Parameters:
- `radius`: Radius for neighbor detection (default: 4)
- `lambda_reg`: Regularization strength for cell proportion estimation (default: 0.001)
- `alpha_elastic`: Elastic net mixing parameter for cell proportion estimation (default: 0.7)
- `max_y_change`: Maximum allowed change in Y values (default: 0.2)

#### Optional Parameters:
- `profiling_only`: Set for cell-type proportions only.
- `max_workers`: Number of parallel workers.
- `checkpoint_interval`: Checkpoint saving interval.

#### B. Using SLURM Distribution
For large-scale analyses, you can use the provided `examples/sbatch_sample.sh` script for distributed computing.

---

## Benchmarking and Reproducibility

For specific reproduction of benchmarking tests and detailed methodology, please refer to the 'examples' and 'benchmarking' section in the documentation.

---

## Run the Analysis

You can either:

#### A. Run the code directly:
- Expected runtime: ~2 hours on a standard computer (16 threads, 32GB RAM).

#### B. Use SLURM distribution:
- Use the provided `examples/sbatch_sample.sh` script for distributed computing.

---

## Additional System Requirements
- **RAM**: 32GB (minimum)
- **CPU**: 16 threads (recommended)
- **Storage**: Sufficient space for your dataset
- **Operating System**: Linux/Unix recommended (Windows users may need additional configuration)
