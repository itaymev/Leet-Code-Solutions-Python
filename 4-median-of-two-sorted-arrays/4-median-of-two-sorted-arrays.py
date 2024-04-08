class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        for i in nums2:
            nums1.append(i)
        nums1.sort()

        # midway point
        mid = len(nums1) // 2

        if len(nums1) % 2 == 0:
            # print("even")
            return (nums1[mid] + nums1[mid-1])/2
        else:
            # print("odd")
            return nums1[mid]

            
solution = Solution()

print(solution.maxArea([1,3], [2])) ## 2.0

print(solution.maxArea([1,2], [3,4])) ## 2.5
