

class StringCalculator:
    def __init__(self):
        pass

    def add(self, numbers):
        if not numbers:
            return 0
        numbers = numbers.replace("\n", ",")
        numbers = numbers.split(",")
        res = sum(int(num) for num in numbers)
        return res