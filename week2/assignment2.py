# Uses python3
import sys

def get_fibonacci_last_digit_naive(n):
        a=0
        b=1
        res = 0
        if n==0:
            return 0
        elif n==1:
            return 1
        for i in range(2, n + 1):
            res = (a + b)%10
            a = b
            b = res
        return res

if __name__ == '__main__':
    input = sys.stdin.read()
    n = int(input)
    print(get_fibonacci_last_digit_naive(n))
