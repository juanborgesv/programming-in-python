import pytest
import addition

def test_add():
    assert addition.add(4, 5) == 9
    assert addition.add(-1, -2) == -3
    assert addition.add(0.5, 0.05) == 0.55

def test_sub():
    assert addition.sub(1, 1) == 0
    assert addition.sub(-1, -1) == 0

# Note: you run the test by typing on the terminal the following:
#   - python -m pytest <path>.py
#   - python -m pytest <path>.py::method_name (test specific method)