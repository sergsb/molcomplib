from rdkit import Chem, DataStructs
from rdkit.Chem import AllChem
import pickle
import numpy as np
import os
ROOT_DIR = os.path.realpath(os.path.join(os.path.dirname(__file__)))

def convert_mol_to_ecfp(mol,r=3, n=2048):
    arr = np.zeros((1, n))
    fp = AllChem.GetMorganFingerprintAsBitVect(mol, r, nBits=n)
    DataStructs.ConvertToNumpyArray(fp, arr)
    return arr

def apply_dense_layer_numpy(x, w, b):
    return x.dot(w) + b

def apply_batchnorm_numpy(x,gamma, beta, running_mean,running_var,eps=1e-5):
    x = (x - running_mean) / np.sqrt(running_var + eps)
    return x*gamma + beta

def apply_relu_numpy(x):
    return np.maximum(x, 0)

class MolCompass:
    def __init__(self,descriptorsType="ecfp_3_2048",modelDescription=None):
        """
        Parameters were added for the compatibility with further versions of MolCompass. Do not use them now.
        :param descriptorsType: Reserved for the future use.
        """
        modelType = 'ecfp3' if descriptorsType == 'ecfp_3_2048' else None
        if not modelType: raise NotImplementedError('Other types of models are not implemented yet')
        #dimensionality ="2d" if dimensionality == '2d' else None
        #if not dimensionality:raise NotImplementedError('3D has not been implemented yet')
        fileName = os.path.join(ROOT_DIR, 'bin', '{}_{}.pkl'.format(descriptorsType, '2d')) #Fixme: add model description
        with open(fileName, "rb") as f:
            self.parameters = pickle.load(f)

    def _apply_ecfp6_2d(self,input):
        for layer in range(1,5):
            w = self.parameters["fc"+str(layer)+".weight"].transpose(1,0)
            b = self.parameters["fc"+str(layer)+".bias"]
            input = apply_dense_layer_numpy(input, w, b)
            if layer != 4:
                input = apply_batchnorm_numpy(input, self.parameters["bn" + str(layer) + ".weight"],
                                            self.parameters["bn" + str(layer) + ".bias"],
                                            self.parameters["bn" + str(layer) + ".running_mean"],
                                            self.parameters["bn" + str(layer) + ".running_var"])
                input = apply_relu_numpy(input)
        return input

    def __call__(self, smiles):
        mol = Chem.MolFromSmiles(smiles)
        ecfpd = convert_mol_to_ecfp(mol)
        return self._apply_ecfp6_2d(ecfpd)

    def process(self, data):
        """
        Multi-tool for processing data.
        :param data: A pandas dataframe with smiles column.
        :return:
        """
        def robust(x):  
            try:
                return self.__call__(x)
            except:
                return np.array([np.NAN,np.NAN],dtype=np.float32) #Fixme: if the dimensionality is 3d, then it should be np.array([np.NAN,np.NAN,np.NAN],dtype=np.float32)

        try:
            import pandas as pd
            if isinstance(data, pd.DataFrame):
                smilesColumn = [x for x in data.columns if x.lower() in ['smiles', 'smiles', 'smiles','canonical_smiles', 'molecules', 'structures','mols','smi']]
                assert len(smilesColumn) == 1, "Dataframe should contain ONLY one smiles column, but found: {}".format(smilesColumn)
                smilesColumn = smilesColumn[0]
                coords = np.vstack(data[smilesColumn].apply(robust).values)
                x = coords[:,0]
                y = coords[:,1]
                return pd.concat([data, pd.DataFrame({"x":x,"y":y})], axis=1)
        except ImportError:
            pass
        except Exception as e:
            raise e

