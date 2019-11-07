


##### merge_sort_04121106.py
class Solution(object):
    def merge_sort(self, nums):#此函數先選出list的中間再以中間去將list分成left right
        self.nums = nums       #再return 回nums
        
        mid=len(nums)//2 #選出list的中間項 我認為直接對半切是最快的方法 雖然有會不太準的時候
        left=nums[:mid]  #但我用奇數列表測試 並無大礙
        right=nums[mid:]       
        
        if len(left)>1:#If the length of the list is less than or equal to one
            Solution().merge_sort(left)
        if len(right)>1:#If the length of the list is less than or equal to one
            Solution().merge_sort(right)
            
            i=0
            j=0
            k=0
            while i<len(left) and j<len(right):#while 的比較迴圈
                if left[i]<=right[j]:#目的讓演算法穩定
                    nums[k]=left[i]
                    i=i+1
                else:
                    nums[k]=right[j]
                    j=j+1
                k=k+1
                
            while i<len(left):
                nums[k]=left[i]
                i=i+1
                k=k+1
                
            while j<len(right):
                nums[k]=right[j]
                j=j+1
                k=k+1
        return nums
    
    #####以同學(from samuel871211)的做比較:
#    class Solution(object):
    
#    def merge_sort(self,nums): 
#        self.nums = nums
        
#        left = nums[0:len(nums)//2]
#        right = nums[len(nums)//2:len(nums)]
    
#        if len(left) > 1:
#           Solution().merge_sort(left)
    
#        if len(right) > 1:
#            Solution().merge_sort(right)
        
#        SortedArray = Solution().merge(nums,left,right) <-這部分有點不明白 會甚麼要多一個SortedArray  多
#        return SortedArray
    
#    def merge(self,nums,left,right): 
    
#        index_left = 0
#        index_right = 0
#        index_nums = 0
    
#        while index_left < len(left) and index_right < len(right): 
#            if left[index_left] < right[index_right]:
#                nums[index_nums] = left[index_left]
#                index_left = index_left + 1
#            elif left[index_left] > right[index_right]:
#                nums[index_nums] = right[index_right]
#                index_right = index_right + 1
#            elif left[index_left] == right[index_right]:
#                nums[index_nums] = left[index_left]
#                index_left = index_left + 1           
#            index_nums = index_nums + 1  
    
#        if index_left < len(left) and index_right == len(right): 
#            for i in range(index_left,len(left)):
#                nums[index_nums] = left[index_left]
#                index_left = index_left + 1
#                index_nums = index_nums + 1
#        elif index_right < len(right) and index_left == len(left): 
#            for i in range(index_right,len(right)):
#                nums[index_nums] = right[index_right]
#                index_right = index_right + 1
#                index_nums = index_nums + 1
# 上方同學的寫法和理解程度讓人敬佩
# 想到了很多 我沒想到要注意的點 不過我覺得有一點複雜 可能是我自己的問題吧哈哈哈






