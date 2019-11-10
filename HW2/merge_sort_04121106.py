#!/usr/bin/env python
# coding: utf-8

# In[10]:


# merge_sort_04121106.py
class Solution(object):
    def merge_sort(self,nums): 
        if len(nums) >1: 
            mid = len(nums)//2 #Finding the mid of the array 
            L = nums[:mid] # Dividing the array elements  
            R = nums[mid:] # into 2 halves 
  
            mergeSort(L) # Sorting the first half 
            mergeSort(R) # Sorting the second half 
  
            i = j = k = 0
          
                # Copy data to temp arrays L[] and R[] 
            while i < len(L) and j < len(R): 
                if L[i] < R[j]: 
                    nums[k] = L[i] 
                    i+=1
                else: 
                    nums[k] = R[j] 
                    j+=1
                k+=1
          
        # Checking if any element was left 
            while i < len(L): 
                nums[k] = L[i] 
                i+=1
                k+=1
          
            while j < len(R): 
                nums[k] = R[j] 
                j+=1
                k+=1
                return nums


# In[12]:


output = Solution().merge_sort([0,0-1,-1,1,1])
output


# In[ ]:




