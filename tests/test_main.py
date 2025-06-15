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
    
    def test_add_unknown_amount_of_numbers_should_return_sum(self):
        assert self.calculator.add("1,2,3,4,5,6,7,8,9,10") == 55
    
    def test_add_new_line_between_numbers_should_return_sum(self): 
        assert self.calculator.add("1\n2,3") == 6
    
    def test_add_different_delimiters_should_return_sum(self):
        assert self.calculator.add("//;\n1;2") == 3
    
    def test_add_negative_numbers_should_raise_exception(self):
        with pytest.raises(ValueError) as e:
            self.calculator.add("1,-2,-3")
        assert "negatives not allowed" in str(e.value)
    
    def test_add_multiple_negative_numbers_should_raise_exception(self):
        with pytest.raises(ValueError) as e:
            self.calculator.add("1,-2,-3,4,-5")
        assert "negatives not allowed" in str(e.value)
        assert "-2,-3,-5" in str(e.value)
    
    def test_get_called_count_should_return_zero(self):
        assert self.calculator.GetCalledCount() == 0
    
    def test_get_called_count_should_return_one(self):
        self.calculator.add("1")
        assert self.calculator.GetCalledCount() == 1
    
    
    def test_get_called_multiple_should_return_correct_count(self):
        self.calculator.add("1")
        self.calculator.add("1, 23")
        self.calculator.add("")
        assert self.calculator.GetCalledCount() == 3
        