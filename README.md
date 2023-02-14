

## Introduction 
<img align="left" src="https://user-images.githubusercontent.com/4963384/218703831-1460bc07-7e9f-417e-9b0c-c9675db5de9f.png"> <p align="justify">
 `Molcomplib` is a key component of the `MolCompass` project. It is a python library, that provides the pretrained parametric t-SNE model for molecular visualization.
This model was trained on ChEMBL data (about 1 Million of molecules). This library generates X and Y coordinates for compounds so that similar compounds group together forming well-recognisible clusters. The library is lightweight, and requires only `rdkit` and `numpy` (optionally, `pandas`) 
 
</p>

<br>

## Installation
You can install it directly from github:

```pip install git+https://github.com/sergsb/molcomplib.git```

or from `PyPi` like normal python package:
``pip install molcomplib``

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
