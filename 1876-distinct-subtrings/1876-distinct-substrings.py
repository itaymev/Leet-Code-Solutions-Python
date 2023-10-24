class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        count = 0

        if (len(s) - 2) > 0:
            for i in range(len(s) - 2):
                if s[i] != s[i+1] and s[i+1] != s[i+2] and s[i] != s[i+2]:
                    ## print(s[i], s[i+1], s[i+2])
                    count += 1

        return count
    
solution = Solution()

string = "aababcabc"
answer1 = solution.countGoodSubstrings(solution, string)
print(answer1)  ## 4

string = "xyzzaz"
answer2 = solution.countGoodSubstrings(solution, string)
print(answer2)  ## 1