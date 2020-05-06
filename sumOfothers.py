from math import fsum
import numpy as np

def other(array):
    sum = []
    for i in range(0,len(array)):
        list = []
        for j in range(0,len(array)):
            if j != i:
                list.append(array[j])
            elif j == i:
                continue
        print(list)
        sum.append(fsum(list))
    print(sum)



if __name__ == '__main__':
    arr= [1,5,3,2,12,7,2]
    other(arr)