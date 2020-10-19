
import numpy

### INSERT ###
# сортування по спаданню, перевернення масиву


def Insert(sort):
    exchange = 0
    comparison = 0
    for i in range(1, len(sort)):

        number = sort[i].copy()

        for j in range(i - 1, -1, -1):
            comparison += 1
            if number[1] >= sort[j][1]:
                break
            
            exchange += 1
            sort[j + 1] = sort[j].copy()
            sort[j] = number
    sort = sort[::-1]
    return sort, exchange, comparison


### INSERT ###
# сортування по спаданню
def Insert_t(sort):
    for i in range(len(sort) - 1, -1, -1):

        number = sort[i].copy()

        for j in range(i + 1, len(sort)):
            if number[2] >= sort[j][2]:
                break

            sort[j - 1] = sort[j]
            sort[j] = number
    return sort


### Merge ###
# сортування по зростанню


def Merge(mass):

    exchange = 0
    comparison = 0

    if len(mass) > 1:
        left = []
        right = []

        for i in range(len(mass) // 2):
            left.append(mass[i])

        for i in range(len(mass) // 2, len(mass)):
            right.append(mass[i])

        left, excl, coml = Merge(left)
        right, excr, comr = Merge(right)


        arr = []

        while True:
            if len(left) > 0 and len(right) > 0:
                comparison += 1
                if left[0][2] > right[0][2]:
                    exchange += 1
                    arr.append(right[0])
                    del right[0]
                else:
                    arr.append(left[0])
                    del left[0]

            elif len(left) > 0 and len(right) == 0:
                arr.append(left[0])
                del left[0]

            elif len(right) > 0 and len(left) == 0:
                arr.append(right[0])
                del right[0]

            else:
                break
        
        exchange += excl + excr
        comparison += coml + comr
        return arr, exchange, comparison

    return mass, exchange, comparison 