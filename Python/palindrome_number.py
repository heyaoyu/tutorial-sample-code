# https://oj.leetcode.com/problems/palindrome-number/

class Solution:

    def getTotal(self, x):
        ret = 1
        while x/10:
            ret += 1
            x = x/10
        return ret

    def getNumAt(self, x, i):
        for j in range(0, i):
            x = x/10
        return x%10

    # @return a boolean
    def isPalindrome(self, x):
        if x<0:
            return False
        total = self.getTotal(x)
        for i in range(total/2):
            first = self.getNumAt(x, i)
            second = self.getNumAt(x, total-i-1)
            if first!=second:
                return False
        return True

print Solution().isPalindrome(1233421)