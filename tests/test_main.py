import sys 
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import pytest
from src.main import StringCalculator


def test_add_empty_string_should_return_zero():
    calculator = StringCalculator()
    assert calculator.add("") == 0