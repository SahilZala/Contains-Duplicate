class Solution(object):
    def containsDuplicate(self, nums):

        for i in range(0,nums.__len__()-1):
            for j in range(i+1,nums.__len__()):
                if nums[i] == nums[j]:
                   return True
        return False


s = Solution()
print(s.containsDuplicate([1,2,3,1]))
