from setuptools import setup

setup(
    # Your setup arguments
    python_requires=">=3.6",  # Your supported Python ranges
    name="molcomplib",
    version="1.1.3",
    description="A library for the projection of chemical compounds onto 2D space, mostly for visualization purposes.",
    long_description="""Molcomplib is a key component of the MolCompass project. It is a python library, that provides the pretrained parametric t-SNE model for molecular visualization. This model was trained on ChEMBL data (about 1 Million of molecules). This library generates X and Y coordinates for compounds so that similar compounds group together forming well-recognisible clusters. The library is lightweight, and requires only rdkit and numpy (optionally, pandas)""",
    author="Sergey Sosnin",
    author_email="sergey.sosnin@univie.ac.at",
    include_package_data=True,
    url="https://github.com/sergsb/molcompview",
    install_requires=[
        "rdkit",
        "numpy",
    ],
    packages=["molcomplib"],
    package_data={"molcomplib": ["bin/*.pkl"]},
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Development Status :: 5 - Production/Stable",
        "Topic :: Scientific/Engineering :: Chemistry",
        "Intended Audience :: Science/Research",
    ],
    keywords="chemistry, cheminformatics, t-SNE, visualization,  chemical space",
    license="MIT",
)
