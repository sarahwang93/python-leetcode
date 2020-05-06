import sys

# sorting method O(nlogn)
class countSolution:
    def majorityElement(self, nums, lo=0, hi=None):
            nums.sort()
            print(nums)
            return nums[len(nums)//2]

if __name__ == "__main__":
    array = [2, 3, 5, 6, 2, 2, 2]
    print(countSolution.majorityElement(countSolution, array, 0, 6))