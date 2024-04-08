class Solution:
    def maxArea(self, height: list[int]) -> int:
        first = 0
        last = len(height) -1
        max_area = 0

        while first < last:
            curr = min(height[first], height[last]) * (last - first)
            if max_area < curr:
                max_area = curr

            if height[first] < height[last]:
                first += 1
            else:
                last -= 1

        return int(max_area)

            
solution = Solution()

print(solution.maxArea([1,8,6,2,5,4,8,3,7])) ## 49

print(solution.maxArea([1,1])) ## 1