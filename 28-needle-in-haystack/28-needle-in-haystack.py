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
answer1 = Solution.removeElement(solution, haystack, needle)
print(answer1) ## 0

needle = "leeto"
haystack = "leetcode"
answer2 = Solution.removeElement(solution, haystack, needle)
print(answer2) ## -1
