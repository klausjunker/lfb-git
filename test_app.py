#import sys
#import os
#sys.path.append(os.path.abspath(".."))
from app import jkadd
from app import jksub

def test_add():
    assert jkadd(2, 3) == 5
    assert jkadd(-1, 1) == 0
def test_sub():
    assert jksub(5, 3) == 2

