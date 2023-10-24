class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        while val in nums:
            nums.remove(val)

solution = Solution()

val = 3
nums = [3,2,2,3] 
Solution.removeElement(solution, nums, val)
print(nums) ## [2, 2]

val = 2
nums = [0,1,2,2,3,0,4,2]
Solution.removeElement(solution, nums, val)
print(nums) ## [0, 1, 3, 0, 4]