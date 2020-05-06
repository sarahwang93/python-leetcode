import sys
from math import fmod

def GCD(a,b):
   if b==0:
        return a
   else:
       return GCD(b, a%b)


if __name__ == '__main__':
    a,b = input().split(" ")
    print(GCD(int(a),int(b)))