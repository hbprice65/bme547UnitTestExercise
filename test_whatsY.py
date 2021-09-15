"""
inputs: 2 tupels (x,y pairs) and 1 x value, floats
output: 1 y value, float
"""
import pytest

@pytest.mark.parametrize("pairs,newx,expectedY",[
    (((1, 2),(2,4)),3,6)
])
def test_sovleForY(pairs,newx, expectedY):
    from whatsY import solveForY
    answer = solveForY(pairs,newx)
    assert answer == expectedY