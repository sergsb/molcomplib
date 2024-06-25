
## Introduction 

<img align="left" src="https://user-images.githubusercontent.com/4963384/218703831-1460bc07-7e9f-417e-9b0c-c9675db5de9f.png"> <p align="justify">
 `Molcomplib` is a key component of the `MolCompass` project. It is a python library, that provides the pretrained parametric t-SNE model for molecular visualization. This library generates X and Y coordinates for compounds so that similar compounds group together forming well-recognisible clusters. The library is lightweight, and requires only `rdkit` and `numpy` (optionally, `pandas`) 
 
</p>

<br>

## Graphical abstract
<img align="left" width="200px" src="https://github.com/sergsb/molcomplib/assets/4963384/ce56961c-8ce0-46eb-ab6a-d66c4be73a6c.png"> 

Application of a Parametric t-SNE model: A set of chemical compounds **(A)** is converted into ECFP binary fingerprints of a fixed length **(B)**. Then, a pretrained artificial neural network (ANN) **(C)** projects these fingerprints into coordinates, forming 2D clusters where structurally similar compounds are grouped together **(D)**

<br>

<br>

## Installation
`pip install molcomplib`


## Usage
Import the libraty and create ``MolCompass `` object:
```
from molcomplib import MolCompass
compass = MolCompass()
```
You can apply it for an individual molecule:
```
print(compass('CCO'))

[ -0.98872091 -35.78184447]
```
Or apply to a list of molecules:
```
list_of_compounds = ['CCC','CCO','C1=CC=C(C=C1)C=O']
res = np.vstack([compass(compound) for compound in list_of_compounds])
print(res)

[[ -1.60652074 -36.25469236]
 [ -0.98872091 -35.78184447]
 [-32.6078482   -7.50528324]]
```

`molcomplib` also provides an interface to pandas interface:

```
from molcomplib import MolCompass
molcomp = MolCompass()
import pandas as pd
df = pd.DataFrame({'smiles':["CCO","CCC"]})
res = molcomp.process(df)
print(res)

        x          y
  smiles         x          y
0    CCO -0.988721 -35.781844
1    CCC -1.606521 -36.254692
```

## Other parts of MolCompass
`molcomplib` is a computational engine for [MolCompass KNIME Node](https://github.com/sergsb/MolCompassKnimeNode) and [MolCompass Viewer GUI tool (molcompview)](https://github.com/sergsb/molcompview).  

## Citation
Please, cite Sosnin S. _MolCompass: Multi-Tool for the Navigation in Chemical Space and Visual Validation of QSAR/QSPR Models_ submitted to Journal of Cheminformatics

## DOI for the package version 
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.12529381.svg)](https://doi.org/10.5281/zenodo.12529381)


