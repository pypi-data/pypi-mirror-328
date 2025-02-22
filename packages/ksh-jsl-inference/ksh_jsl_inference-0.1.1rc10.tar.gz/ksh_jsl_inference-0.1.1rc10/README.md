# endpoints


## Development

### Pre-requisites

- Python 3.8 or higher
- Docker
- A valid JSL License

### Setup
```bash
 pip install -r dev-requirements.txt
```

### CLI


To install the package locally, run the following command from the root of the repository:

```bash
 cd endpoints
 python3 -m pip install -e .
```

This will install the `jsl_inference` CLI command defined in `pyproject.toml`.

Alternatively, if you haven't defined the `jsl_inference` script in `pyproject.toml` or `setup.py`, you can run the CLI directly:

```bash
 python -m endpoints.cli
```

## Docs

Documentation is generated using Sphinx. To generate the documentation, run:

```bash
 cd docs
 make html
```
This will generate the documentation in the `docs/build/html` directory. Open `docs/build/html/index.html` in a browser to view the documentation.

### Testing
Install the test requirements, along with the dev requirements
```bash
 pip install -r dev-requirements.txt -r test-requirements.txt
```

To run the tests, run the following command:

```bash
 pytest
```

### Toolkit

To get some information on the available models and its details, use this helper command

<small>Please make sure to install dependencies before. See tools/requirements.txt </small>
```bash
 python tools/models_info.py
```
You can also refer the help for this toolkit

```bash
 python tools/models_info.py --help
```




## Databricks Development (Needs to fixed)

see `databricks_tests.py` 
1. Start up a Databricks Cluster producer. Once Started you must **manually enable it to Unity Catalog**
2. Submit publisher job
3. Once completed, need to go to provider UI and publish the model to either private or public exchange
4. Once published, **you must manually import the listing on consumer end form the UI and accept the Terms of usage**. Then model can be tested via consumer jobs

