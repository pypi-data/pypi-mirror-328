# tqml

![python](https://img.shields.io/badge/python-%5E3.9.0-blue)
![pennylane](https://img.shields.io/badge/pennylane-%5E0.29.1-blue)
![torch](https://img.shields.io/badge/torch-%5E2.0.0-blue)

Python module with useful quantum tools for Hybrid NNs based
on `pennylane` and `torch` frameworks.

## Installation

Choose one of **five options**.
- The first one is **preferred** for common usage by TQ members.
- The second one is for people outside of TQ (WIP).
- The last is recommended only for *developers*.

### **From GCP Artifact registry**
1) Create new `conda` environment to prevent conflicts with previous versions of your packages
    ```bash
    conda create -n tqml python=3.9
    conda activate tqml
    ```
2) Make sure you have access to GCP (take a look if GCP shows up in your Jumpcloud Console)
3) Make sure you are logged in with the google cloud CLI
   ```bash
   gcloud auth application-default login
   ```

4) Use pip or poetry to install the package with the specification of the external registry.
   ```bash
   pip install --extra-index-url https://europe-python.pkg.dev/cryptic-hawk-387713/tq-core/simple tqml
   ```

**NOTE**: This currently only includes any package versions starting from version 4.0.2

### **Licensed public release**

1) Create new `conda` environment to prevent conflicts with previous versions of your packages
    ```bash
    conda create -n tqml python=3.9
    conda activate tqml
    ```

2) Use pip or poetry to install the package (optionally with a specific version).
   ```bash
   pip install tqml==5.9.1
   ```

   **NOTE**: This currently only includes any package versions starting from version 5.9.1

3) You need to provide a valid license key via the env variable `TQML_LICENSE_KEY`. To retrieve your (previously requested) license keys please go to [TQ License portal](https://terraquantum.io/licenses).

   **NOTE**: You need to be assigned a license key by the TQ team to use this package. Please get in touch with [support@terraquantum.swiss](mailto:support@terraquantum.swiss).

4) You can now use the package as usual.


### **From GitHub Repository**
1) Create new `conda` environment to prevent conflicts with previous versions of your packages
    ```bash
    conda create -n tqml python=3.9
    conda activate tqml
    ```
2) Access remote repository with `pip+ssh`. Make sure that you have added your `ssh` credentials to your GitHun account.
   ```bash
   pip install git+ssh://git@github.com/terra-quantum-io/tqml.git
   ```
   You can also specify exact version for installation with `@vX.Y.Z`. For example if you want to install `v2.3.1`:
   ```bash
   pip install git+ssh://git@github.com/terra-quantum-io/tqml.git@v2.3.1
   ```

### **From GitHub Releases**
1) Go to [latest release](https://github.com/terra-quantum-io/TQnet/releases/latest) and proceed to **Assets**. There you can find `.whl`
file. Download it and place in preferred directory for further installation.
2) Create new `conda` environment to prevent conflicts with previous versions of your packages
    ```bash
    conda create -n tqml python=3.9
    conda activate tqml
    ```
3) Run in `tqnet` environment
    ```bash
    pip install --upgrade tqml-x.y.z-py3-none-any.whl
    ```

### **With tests and `poetry`** (for developers)
1) Create `conda` environment with Python3.9 and activate it
2) Install `poetry` with on Linux
    ```bash
    curl -sSL https://install.python-poetry.org | python3 -
    ```
3) Go to repo's directory, initialize `poetry` and run tests
    ```bash
    cd TQnet
    poetry install
    ```
4) If you want. you can run tests to ensure that everything is OK
    ```bash
    pytest tests
    ```
5) Build your package
    ```bash
    poetry build
    ```
6) Install package via `pip`
    ```bash
    pip install .\dist\tqnet-0.4.1-py3-none-any.whl
    ```


## Documentation and support

You can find documentation and API reference for this package on
[GitHub Pages](https://refactored-train-y27rprg.pages.github.io/). Please, be free to report bugs and leave feedback in
[Issues](https://github.com/terra-quantum-io/tqml/issues).

## Usage

```python
from tqml.tqnet.layers import QDI
import torch

layer = QDI(
   in_features=20,
   n_qubits=4,
   depth=4,
   entangling='basic',
   rotation='Y',
   measurement_mode='single',
   measure='Y'
)

inputs = torch.rand((10, 20))
outputs = layer(inputs)

assert outputs.shape == (10, 1)
```

## Contributing

Interested in contributing? Check out the contributing guidelines. Please note that this project is released with a Code of Conduct. By contributing to this project, you agree to abide by its terms.

## License

`tqml` was created by Terra Quantum.
