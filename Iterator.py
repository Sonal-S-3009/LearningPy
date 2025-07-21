class Countdown:
    def __init__(self, start):
        self.start = start

    def __iter__(self):
        return CountdownIterator(self.start)

class CountdownIterator:
    def __init__(self, current):
        self.current = current

    def __iter__(self):
        return self  # iterators return themselves

    def __next__(self):
        if self.current <= 0:
            raise StopIteration
        else:
            val = self.current
            self.current -= 1
            return val

for number in Countdown(3):
    print(number)
