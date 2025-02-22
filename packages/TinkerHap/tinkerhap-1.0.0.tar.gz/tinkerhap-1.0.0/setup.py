from setuptools import setup, find_packages

with open("README.md", "r") as f:
    description = f.read()

setup(
    name="TinkerHap",
    version="1.0.0",
    author="Uri Hartmann", 
    packages=find_packages(),
    entry_points={
        "console_scripts": [
            "tinkerhap=tinkerhap.tinkerhap:main",
        ],
    },
    install_requires=[
        'pysam>=0.17.0'
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Topic :: Scientific/Engineering :: Bio-Informatics",
    ],
    python_requires=">=3.6.0",
    long_description=description,
    long_description_content_type="text/markdown",
    license="MIT"
)
