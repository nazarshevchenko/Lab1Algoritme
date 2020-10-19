
import pandas
import numpy
from algoritme import *
import time

data = pandas.read_csv("data.csv")

sort = data.to_numpy()

#print(sort)
#print()



t = time.time()

print("******")
print("INSERT")
t = time.time()

insert, exchange, comparison = Insert(sort)

for i in range(10):
    print(insert[i])

print("time = " + str(time.time() - t))
print("exchange = {}".format(exchange))
print("comparison = {}".format(comparison))
print("******")


print("Merge")
t = time.time()

merge, exchange, comparison = Merge(sort)

for i in range(10):
    print(merge[i])

print("time = " + str(time.time() - t))
print("exchange = {}".format(exchange))
print("comparison = {}".format(comparison))


pandas.DataFrame(insert).to_csv("insert.csv", index=False)

pandas.DataFrame(merge).to_csv("merge.csv", index=False)







