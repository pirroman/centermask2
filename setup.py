from os import path
from setuptools import find_packages, setup


def get_version():
    init_py_path = path.join(
        path.abspath(path.dirname(__file__)), "centermask", "__init__.py"
    )
    init_py = open(init_py_path, "r").readlines()
    version_line = [l.strip() for l in init_py if l.startswith("__version__")][0]
    version = version_line.split("=")[-1].strip().strip("'\"")

    return version


setup(
    name="centermask2",
    version=get_version(),
    author="",
    url="https://github.com/pirroman/centermask2",
    description="CenterMask2 is an upgraded implementation on top of detectron2 beyond original CenterMask based on "
    "maskrcnn-benchmark. "
    "platform for object detection and segmentation.",
    packages=find_packages(exclude=("configs", "demo", "datasets")),
    python_requires=">=3.6",
    install_requires=["detectron2"],
    include_package_data=True,
    zip_safe=False,
)
