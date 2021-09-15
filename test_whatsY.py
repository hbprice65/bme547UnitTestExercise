"""
inputs: 2 tupels (x,y pairs) and 1 x value, floats
output: 1 y value, float
"""
import pytest

@pytest.mark.parametrize("pair1,pair2,newx,expectedY",[
    ((1,2),(2,4),3,6)
])
def test_solveForY(pair1,pair2,newx, expectedY):
    from whatsY import solveForY
    answer = solveForY(pairs,newx)
    assert answer == expectedY