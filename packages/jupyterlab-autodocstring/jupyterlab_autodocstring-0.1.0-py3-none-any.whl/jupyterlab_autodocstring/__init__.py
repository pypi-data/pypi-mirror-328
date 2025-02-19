import json
import os
from jupyterlab.labhubapp import LabApp

try:
    from ._version import __version__
except ImportError:
    # Fallback when using the package in dev mode without installing
    # in editable mode with pip. It is highly recommended to install
    # the package from a stable release or in editable mode: https://pip.pypa.io/en/stable/topics/local-project-installs/#editable-installs
    import warnings
    warnings.warn("Importing 'jupyterlab_autodocstring' outside a proper installation.")
    __version__ = "dev"

# Load the extension's metadata from package.json
HERE = os.path.dirname(__file__)
with open(os.path.join(HERE, "..", "package.json")) as f:
    package_json = json.load(f)
    __version__ = package_json["version"]

def _jupyter_labextension_paths():
    return [{
        "src": "labextension",
        "dest": package_json["name"]
    }]
