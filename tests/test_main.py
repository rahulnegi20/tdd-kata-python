import sys 
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import pytest
from src.main import StringCalculator

class TestStringCalculator:
    def setup_method(self):
        self.calculator = StringCalculator()

    def test_add_empty_string_should_return_zero(self):
        assert self.calculator.add("") == 0


    def test_add_single_number_should_return_number(self):
        assert self.calculator.add("1") == 1

    def test_add_two_numbers_should_return_sum(self):
        assert self.calculator.add("1,2") == 3

    def test_add_multiple_numbers_should_return_sum(self):
        assert self.calculator.add("1,2,3,4,5") == 15