class Solution:
    def twoSum(self, nums, target):
        for i in range(len(nums)-1):
            for j in range(i+1,len(nums)-1):
                if nums[i] + nums[j]==target:
                    print(i,j)
        
obj=Solution()
nums=[3,2,4]
target=6
print(obj.twoSum(nums,target))
