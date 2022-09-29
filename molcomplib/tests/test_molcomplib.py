import pytest

def test_molcomplib_import():
    from molcomplib import MolCompass
    assert True

def test_molcomplib_apply():
    from molcomplib import MolCompass
    molcomp = MolCompass()
    assert molcomp("CCO") is not None

def test_molcomplib_single():
    from molcomplib import MolCompass
    molcomp = MolCompass()
    res =  molcomp("CCO")
    #it should be [ -0.98872091 -35.78184447]
    assert res[0] == pytest.approx(-0.98872091)
    assert res[1] == pytest.approx(-35.78184447)

def test_pandas():
    from molcomplib import MolCompass
    molcomp = MolCompass()
    import pandas as pd
    df = pd.DataFrame({'smiles':["CCO","CCC"]})
    res = molcomp.process(df)
    assert res is not None



