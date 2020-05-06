import sys

def get_fibonacci_huge(n,m):
    if n<=1:
        return 1
    arr = [0,1]
    previousmod = 0
    currentmod = 1

    for i in range(n-1):
        tempMod = previousmod
        previousmod = currentmod % m
        currentmod = (tempMod + currentmod) % m
        #cal result on array
        arr.append(currentmod)
        if currentmod == 1 and previousmod == 0:
            index = (n % (i+1))
            return arr[index]
    return currentmod

if __name__ == "__main__":
    n,m = input().split(" ")
    print(get_fibonacci_huge(int(n),int(m)))

