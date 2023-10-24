class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if needle in haystack:
            return haystack.index(needle)
        else:
            return -1
        
solution = Solution()

needle = "sad"
haystack = "sadbutsad" 
Solution.removeElement(solution, haystack, needle)
print(haystack) ## 0

needle = "leeto"
haystack = "leetcode"
Solution.removeElement(solution, haystack, needle)
print(haystack) ## -1