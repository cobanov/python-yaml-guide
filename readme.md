# Python YAML Configuration Guide

YAML (YAML Ain't Markup Language) is a human-readable data serialization format that is commonly used for configuration files and data exchange between programming languages. Python has built-in support for parsing YAML files using the yaml module, which provides functions for reading and writing YAML data.

## Install and Import YAML

```bash
pip install PyYAML
```

After the package installation, you can proceed to import the PyYAML package in Python.

```python
import yaml
```

## Loading YAML with Python

In this example, we open the file config.yaml in read mode and pass it to the yaml.load() function. We also specify the Loader parameter as yaml.FullLoader, which is a safe loader that can load any YAML document.

```python
with open("config.yaml") as f:
    cfg = yaml.load(f, Loader=yaml.FullLoader)
```

## Printing Config

```python
print(cfg)
```

```python
{'maintainer': 'Mert Cobanov',
 'pca_params': {'n_components': 224},
 'umap_params': {'metrics': ['euclidean', 'l1', 'manhattan', 'chebyshev'],
                 'min_dist': [0.01, 0.1, 0.5],
                 'spread': 1.0},
 'visualize_params': {'median_threshold': 6}}
```

## Individual

```python
print(config['pca_params'])

#'n_components': 224
```


## Updating YAML with Python

Updating a YAML configuration file with Python involves loading the existing configuration data, modifying it in memory, and then writing the updated data back to the file. This can be accomplished using the pyyaml library, which provides functions for reading and writing YAML data.

Here's an example of how to update a YAML file using Python:

```python
cfg["n_components"] = 0.2
cfg["umap_params"]["metrics"].append("chebyshev")
```

```python
with open("config.yaml", "w") as f:
    cfg = yaml.dump(
        cfg, stream=f, default_flow_style=False, sort_keys=False
    )
```

It's important to note that the yaml.dump() function will overwrite the entire contents of the file, so you should be careful to include all of the data that you want to keep in the updated file. If you only want to update a specific section of the YAML data, you can modify just that section in memory and then write the entire data structure back to the file.
