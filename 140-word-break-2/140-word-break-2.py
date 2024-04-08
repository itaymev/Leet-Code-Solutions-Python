class Solution:
    def wordBreak(self, s: str, wordDict: list[str]) -> list[str]:
        cache={}
        def wordbr(s):
            if s not in cache: 
                result=[]
                for w in wordDict:
                    if s[:len(w)]==w:
                        if len(s)==len(w):
                            result.append(w)
                        else:
                            for word in wordbr(s[len(w):]):
                                result.append(w+" "+word)
                cache[s]=result
            return cache[s]
        
        return wordbr(s)

            
solution = Solution()

print(solution.maxArea("catsanddog", ["cat","cats","and","sand","dog"])) ## ["cat sand dog","cats and dog"]

print(solution.maxArea("pineapplepenapple", ["apple","pen","applepen","pine","pineapple"])) ## ["pine apple pen apple","pine applepen apple","pineapple pen apple"]
