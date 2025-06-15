

class StringCalculator:
    def __init__(self):
        pass

    def add(self, numbers):
        if not numbers:
            return 0
        delimiter = ","
        if numbers.startswith("//"):
            delimiter_section, numbers = numbers.split("\n")
            delimiter = delimiter_section[2:]
        
        numbers = numbers.replace("\n", delimiter)
        res = sum(int(num) for num in numbers.split(delimiter))
        return res