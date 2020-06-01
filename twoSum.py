from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = {}
        for i, num in enumerate(nums):
            if target - num in dic:
                return [dic[target - num],i]
                break
            dic[num] = i

if __name__ == "__main__":
    test  = [3,2,4]
    target = 6
    print(Solution.twoSum(Solution, test, target))