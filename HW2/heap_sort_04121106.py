#!/usr/bin/env python
# coding: utf-8

# In[27]:


class Solution(object):
    def heap_sort(self, nums):
        self.nums=nums
        arr=Solution().swap(nums)
        return arr
    
         
    def swap(self,nums):
        
        n = len(nums)
        for i in range((n//2)-1,-1,-1): #set the max range of the list
            Solution().heapify(nums, n, i) 
            
    
        
        for i in range(n-1, 0, -1): #swap
            nums[0], nums[i] = nums[i], nums[0]   
            Solution().heapify(nums, i, 0)
        return nums
    def heapify(self,nums, n, i): #basic logic define
        largest = i   
        l = 2 * i + 1     #left=2*i+1
        r = 2 * i + 2     #right=2*i+2
  
    
        if l < n and nums[i] < nums[l]: 
            largest = l 
            
    
        if r < n and nums[largest] < nums[r]: 
            largest = r 
  
    
        if largest != i: 
            nums[largest],nums[i] = nums[i],nums[largest]  
  
        
            Solution().heapify(nums, n, largest)
 


# In[28]:


output=Solution().heap_sort([7,5,8,25,28,3])
output


# In[ ]:




