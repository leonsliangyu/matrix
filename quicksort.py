# -*- coding: utf-8 -*-
# Quick Sort


import random

def partition(nums, start, end):
    pivot = nums[end]
    i = start - 1
    for j in range(start, end):
        if (nums[j] < pivot):
            i += 1;
            nums[i], nums[j] = nums[j], nums[i]
    nums[i+1], nums[end] = nums[end], nums[i+1]
    return (i + 1)    

def qSort(nums, start, end):
    if start < end:
        pi = partition(nums, start, end)
        qSort(nums, start, pi - 1) 
        qSort(nums, pi + 1, end)
    return nums

def quickSort(nums):
    return qSort(nums, 0, len(nums)-1)

nums = random.sample(range(1, 1000), 20)
print(str(nums) + "\n")
print(quickSort(nums))