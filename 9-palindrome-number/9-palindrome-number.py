class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        
        x = str(x)

        # print(x)
        
        if len(x) == 1:
            return True
        elif len(x) == 2:
            if x[0] == x[len(x)-1]:
                return True
            else:
                return False
        else:
            if x[0] == x[len(x)-1]:
                if len(str(int(x[1:len(x)-1]))) < len(x[1:len(x)-1]):
                    return False
                else:
                    return self.isPalindrome(int(x[1:len(x)-1]))
            else:
                return False 
            
solution = Solution()

print(solution.isPalindrome(12321)) ## True

print(solution.isPalindrome(123)) ## False