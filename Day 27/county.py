class Count:

    def __init__(self, max_value):
        self.number = 1
        self.max_value = max_value

    def __iter__(self):
        return self

    def __next__(self):

        if self.number <= self.max_value:
            value = self.number
            self.number += 1
            return value

        raise StopIteration


counter = Count(5)

for number in counter:
    print(number)