from setuptools import setup
from setuptools import find_packages

import numpy


with open("README.md", "rt") as f:
    long_description = f.read()


setup(
    name="pytorchltr2",
    version="0.2.3",
    description="Learning to Rank with PyTorch (Fork of pytorchltr)",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/akreuzer/pytorchltr",
    author="Alexander Kreuzer (original author Rolf Jagerman)",
    author_email="a_kreuzer@posteo.de",
    license="MIT",
    packages=find_packages(exclude=("tests", "tests.*",)),
    python_requires='>=3.10',
    include_dirs=[numpy.get_include()],
    install_requires=["numpy",
                      "scikit-learn",
                      "scipy",
                      "torch"],
    tests_require=["pytest"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_data = {
        "pytorchltr": ["py.typed"],
    },
)
