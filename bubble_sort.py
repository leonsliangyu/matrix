# -*- coding: utf-8 -*-
# Python Bubble Sort Algorithm

import random

def sort(nums):
    finish = False
    j = len(nums)-1
    while finish == False:
        finish = True
        for i in range(j):
            if nums[i] > nums[i+1]:
                t = nums[i]
                nums[i] = nums[i+1]
                nums[i+1] = t 
                k = i
                finish = False 
        j = k
    return nums
        
#input_str = input("Enter a list numbers separated by space: ")
#ints = [int(i) for i in input_str.split()]

nums = random.sample(range(1, 1000), 15)
print("random number list:" + str(nums))
print("\n"+"sorted: " + str(sort(nums)))