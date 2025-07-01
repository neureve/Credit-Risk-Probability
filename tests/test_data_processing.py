import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Fix Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.data_processing import multiply_by_two

def test_multiply_by_two():
    assert multiply_by_two(3) == 6
    assert multiply_by_two(0) == 0
    assert multiply_by_two(-2) == -4
