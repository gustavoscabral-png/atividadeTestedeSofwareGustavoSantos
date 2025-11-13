from eficiencia_motor import *

def test_calcular_eficiencia():
    assert calcular_eficiencia (900,1000) == 90
    assert calcular_eficiencia (855,1000) == 85.5