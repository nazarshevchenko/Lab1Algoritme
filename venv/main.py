
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

insert = Insert(sort)
for i in range(10):
    print(insert[i])
print("time = " + str(time.time() - t))
print("******")
print("Merge")
t = time.time()
merge = numpy.array(Merge(sort))
for i in range(10):
    print(merge[i])
print("time = " + str(time.time() - t))


pandas.DataFrame(insert).to_csv("insert.csv", index=False)

pandas.DataFrame(merge).to_csv("merge.csv", index=False)



#print(sort)




