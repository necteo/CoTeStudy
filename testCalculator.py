# testCalculator.py

class Calculator:
    def __init__(self, nums):
        self.numbers = nums

    def sum(self):
        print(sum(self.numbers))

    def avg(self):
        print(sum(self.numbers) / len(self.numbers))
