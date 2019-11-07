#!/usr/bin/env python
# coding: utf-8

# In[329]:

### heap_sort_04121106.py
class Solution(object):
    def heap_sort(self, nums):
        self.nums=nums

   
        n = len(nums) 
        
    
        for i in range((n//2)-1,-1,-1): #set the max heap of whatever thelist was given
            heapify(nums, n, i) 
            
    
        
        for i in range(n-1, 0, -1): #swap
            nums[0], nums[i] = nums[i], nums[0]   
            heapify(nums, i, 0)
        return nums
    def heapify(self,nums, n, i): #logic define
        largest = i   
        l = 2 * i + 1     #left=2*i+1
        r = 2 * i + 2     #right=2*i+2
  
    
        if l < n and nums[i] < nums[l]: 
            largest = l 
            
    
        if r < n and nums[largest] < nums[r]: 
            largest = r 
  
    
        if largest != i: 
            nums[largest],nums[i] = nums[i],nums[largest]  
  
        
            heapify(nums, n, largest)
 


# In[331]:






