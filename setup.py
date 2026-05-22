# read the contents of your README file
from os import path

from setuptools import find_packages, setup

this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, "README.md"), encoding="utf-8") as f:
    lines = f.readlines()

# remove images from README
lines = [x for x in lines if ".png" not in x]
long_description = "".join(lines)

setup(
    name="praxis-robocasa",
    packages=[package for package in find_packages() if package.startswith("robocasa")],
    install_requires=[
        "numpy==2.2.5",
        "numba==0.61.2",
        "scipy==1.15.3",
        "mujoco==3.3.1",
        "pygame",
        "Pillow",
        "opencv-python",
        "pyyaml",
        "pynput",
        "tqdm",
        "termcolor",
        "imageio",
        "h5py",
        "lxml",
        "hidapi",
        "gymnasium",
        "praxis-robosuite>=1.5.2,<1.6",
    ],
    eager_resources=["*"],
    include_package_data=True,
    python_requires=">=3",
    description="RoboCasa365: A Large-Scale Simulation Framework for Training and Benchmarking Generalist Robots",
    author="Soroush Nasiriany, Sepehr Nasiriany, Abhiram Maddukuri, Yuke Zhu",
    url="https://github.com/Chaoqi-LIU/robocasa",
    author_email="soroush@cs.utexas.edu",
    maintainer="Chaoqi Liu",
    maintainer_email="liuchaoqi730@gmail.com",
    project_urls={
        "Source": "https://github.com/Chaoqi-LIU/robocasa",
        "Maintainer Website": "https://chaoqi-liu.com",
    },
    version="1.0.0",
    long_description=long_description,
    long_description_content_type="text/markdown",
)
