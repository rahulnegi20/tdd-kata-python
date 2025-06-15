

class StringCalculator:
    def __init__(self):
        pass

    def add(self, numbers):
        if not numbers:
            return 0
        
        delimiter = ","
        if numbers.startswith("//"):
            delimiter_section, numbers = numbers.split("\n")
            print(delimiter_section, numbers)
            delimiter = delimiter_section[2:]
        
        numbers = numbers.replace("\n", delimiter)
        nums =  numbers.split(delimiter)
        negative_numbers = [str(num) for num in nums if int(num) < 0]
        if negative_numbers:
            raise ValueError(f"negatives not allowed: {','.join(negative_numbers)}")
        
        res = sum(int(num) for num in nums)
        return res