from typing import List


def rotate(nums: List[int], k: int) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """
    tmp = []
    for i in range(len(nums)-k,len(nums)):
        nums.pop(nums[i])
        tmp.append(nums[i])


    for j in nums:
        tmp.append(j)

    print(nums)


if __name__ == "__main__":
    nums = [1,2,3,4,5,6,7]
    rotate(nums,3)
