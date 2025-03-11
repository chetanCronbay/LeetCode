from typing import List


def maxArea(height: List[int]) -> int:
    ptr1 = 0
    ptr2 = len(height) - 1
    actH = 0
    area = 0 
    
    while ptr1 <= ptr2:
        actH = height[ptr1] if height[ptr1] < height[ptr2] else height[ptr2]
        area = max(area, (ptr2 - ptr1) * actH)
        
        if height[ptr1] > height[ptr2]:
            ptr2 += -1
        
        else:
            ptr1 +=1

    print(area)




maxArea(height = [1,8,6,2,5,4,8,3,7])