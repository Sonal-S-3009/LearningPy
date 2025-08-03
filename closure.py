'''class Average:
    def __init__(self):
        self.series = []

    def __call__(self, new_value):
        self.series.append(new_value)
        sum_values = sum(self.series)
        return sum_values/len(self.series)

avg = Average()
print(avg(10))
print(avg(5))'''

def make_average():
    series = []
    def average(value):
        series.append(value)
        sum_values = sum(series)
        return sum_values/len(series)
    return average

avg = make_average()
print(avg(5))
print(avg(10))

print(avg.__closure__[0].cell_contents)