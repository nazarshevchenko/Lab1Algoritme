import numpy
import pandas
import random

def name():
    l = random.randint(3, 10)
    Name = []
    for i in range(l):
        Name.append(chr(random.randint(65, 90)))
    return ''.join(Name)

def memory():
    return random.randint(1000, 100000)

def zoom():
    return random.randint(1, 200)

arr = []
for i in range(5000):
    arr.append([name(), memory(), zoom()])

arr = numpy.array(arr)

pandas.DataFrame(arr).to_csv("data.csv", index=False)