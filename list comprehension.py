import time

'''# For loop
start = time.time()
result = []
for i in range(10_000_000):
    result.append(i * 2)
print("For loop:", time.time() - start)

# List comprehension
start = time.time()
result = [i * 2 for i in range(10_000_000)]
print("List comp:", time.time() - start)
'''


import time

data = list(range(1_000_000))

# Manual tracking
start = time.time()
i = 0
for val in data:
    i += 1
end = time.time()
print("Manual:", end - start)

# Using enumerate
start = time.time()
for i, val in enumerate(data):
    pass
end = time.time()
print("Enumerate:", end - start)
