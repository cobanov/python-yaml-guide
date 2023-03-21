import yaml
from pprint import pprint

with open("config.yaml") as f:
    cfg = yaml.load(f, Loader=yaml.FullLoader)


pprint(cfg["pca-params"])

cfg["n_components"] = 0.2
cfg["umap_params"]["metrics"].append("chebyshev")

with open("config.yaml", "w") as f:
    cfg = yaml.dump(cfg, stream=f, default_flow_style=False, sort_keys=False)
