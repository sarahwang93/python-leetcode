from typing import List


def containsDuplicate(nums: List[int]) -> bool:
    dic = {}
    detect = False
    for i,n in enumerate(nums):
        if n in dic.values() :
            detect = True
        else:
            dic[i] = n
    return detect

if __name__ == '__main__':
    nums = [2,14,18,22,22]
    print(containsDuplicate(nums))
