from typing import List


def intersect(nums1:List[int], nums2:List[int]) -> List[int]:
    nums1.sort()
    nums2.sort()

    p1 = p2 =0
    result = []

    while p1<len(nums1) and p2<len(nums2):
        num1 = nums1[p1]
        num2 = nums2[p2]
        if num1 > num2:
                p2+=1
        elif num1 < num2:
                p1+=1
        else:
            result.append(num1)
            p1 += 1
            p2 += 1
    return result

if __name__ == "__main__":
    test1 = [1,2,2,1]
    test2 = [1,1]

    print(intersect(test1,test2))