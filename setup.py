from setuptools import setup

setup(
    # Your setup arguments
    python_requires='>=3.6',  # Your supported Python ranges
    name = "molcomplib",
    version = "1.0.0",
    description = "A python library and the standatrized model for the navigation in chemical space. It consists of parametric t-SNE model pretrained on large dataset of bioactive compounds"
                  "This library is a part of MolCompass project. ",
    author = "Sergey Sosnin <serg.sosnin@gmail.com>",
    include_package_data=True,
    install_requires=[
        'rdkit',
        'numpy',
    ],
    packages=["molcomplib"],
    package_data={
        "molcomplib": ["bin/*.pkl"]
    },
    license = "MIT",
)
