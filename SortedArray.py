from typing import List

def findMedianSortedArrays(nums1: List[int], nums2: List[int]) -> float:
    nums3 = nums1 + nums2
    nums3.sort()
    median = (len(nums3) - 1) // 2

    if (len(nums3) - 1) % 2 != 0:
        median2 = median +1

        print((nums3[median] + nums3[median2]) / 2)
    
    else:
        print(nums3[median])


findMedianSortedArrays(nums1 = [1,3], nums2 = [2,4])