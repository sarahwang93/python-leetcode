from typing import List


def plusOne(digits: List[int]) -> List[int]:
    bit = 10
    sum = 0
    for i in range(0, len(digits)):
        if i != len(digits) - 1:
            times = len(digits) - 1 - i
            sum += digits[i] * (bit ** times)
        else:
            sum += digits[i] + 1

    return sum

if __name__ == "__main__":
    dig = [1,2,3]
    print(plusOne(dig))
