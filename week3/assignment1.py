import sys

#money change
coins = [1,5,10]

def moneyChange(value):
    num = 1
    remain = value
    for i in reversed(coins):
        while remain > i:
            remain -= i
            num += 1
    return num

if __name__ == '__main__':
    pendingVal = int(input())
    print(moneyChange(pendingVal))
