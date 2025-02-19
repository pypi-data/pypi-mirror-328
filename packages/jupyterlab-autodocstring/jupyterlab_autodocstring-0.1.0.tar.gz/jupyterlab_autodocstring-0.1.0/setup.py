from setuptools import setup
import json

# Read the package name and version from package.json
with open("package.json") as f:
    package_json = json.load(f)
    labextension_name = package_json["name"]
    version = package_json["version"]

setup(
    name="jupyterlab-autodocstring",
    version=version,
    description="Automatically insert docstring templates in JupyterLab notebooks.",
    author="Your Name",
    author_email="your.email@example.com",
    license="MIT",
    packages=["jupyterlab_autodocstring"],
    include_package_data=True,
    install_requires=["jupyterlab>=3.0"],
    zip_safe=False,
    classifiers=[
        "Framework :: Jupyter",
        "Programming Language :: Python :: 3",
    ],
    keywords=["jupyterlab", "extension", "docstring", "python", "autodocstring"],
    entry_points={
        "jupyterlab.extension": [
            f"{labextension_name} = jupyterlab_autodocstring"
        ],
    },
)
