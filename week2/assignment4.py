import sys

def LCM(a, b):
    result = 0
    arr = []

    if a==1:
        result = b
    elif b==1:
        result = a

    for i in range(max(a,b), a*b+1):
        if i%a == 0 and i%b == 0:
            return i
        else:
            continue
        i -= 1


if __name__ == '__main__':
    a,b = input().split(" ")
    print(LCM(int(a),int(b)))