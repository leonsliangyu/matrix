# -*- coding: utf-8 -*-
# merge-sort

import random

def mergesort(nums):

    less = []
    equal = []
    greater = []

    if len(nums) > 1:
        pivot = nums[0]
        for x in nums:
            if x < pivot:
                less.append(x)
            elif x == pivot:
                equal.append(x)
            elif x > pivot:
                greater.append(x)
    
        return mergesort(less) + equal + mergesort(greater)
    else: 
        return nums

nums = random.sample(range(1, 1000), 20)

print(str(nums) + "\n")
print(mergesort(nums))