import re
class StringCalculator:
    def __init__(self):
        self.counter = 0
        pass

    def add(self, numbers):
        self.counter += 1
        if not numbers:
            return 0
        
        delimiter = ","
        if numbers.startswith("//"):
            delimiter_section, numbers = numbers.split("\n", 1)
            if delimiter_section.startswith("//["):
                #complex delimiter
                delimiters = re.findall(r'\[(.*?)\]', delimiter_section)
                delimiter = "|".join(map(re.escape, delimiters))
            else:
                #simple
                delimiter = delimiter_section[2:]
            
        
        numbers = numbers.replace("\n", delimiter)
        nums = [int(num) for num in re.split(delimiter, numbers)]
        negative_numbers = [str(num) for num in nums if int(num) < 0]
        if negative_numbers:
            raise ValueError(f"negatives not allowed: {','.join(negative_numbers)}")
        
        res = sum(int(num) for num in nums if int(num) <= 1000)
        return res


    def GetCalledCount(self):
        return self.counter