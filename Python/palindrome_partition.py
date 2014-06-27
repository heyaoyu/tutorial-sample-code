# https://oj.leetcode.com/problems/palindrome-partitioning/

class Solution:

    def copy(self, item):
        return [i for i in item]

    def partition(self, s):
        ret = []
        item = []
        return self.sub_partition(ret, item, s)

    def is_palindrome(self, s):
        if s is not None:
            ret = True
            j = 0
            for i in range(len(s)/2):
                j = len(s)-i-1
                if s[i] != s[j]:
                    ret = False
                    break
            return ret
        return False

    def sub_partition(self, ret, item, s):
        if self.is_palindrome(s):
            item_dup = self.copy(item)
            item.append(s)
            ret.append(item)
            item = item_dup
        for i in range(1,len(s)):
            head = s[:i]
            tail = s[i:]
            if self.is_palindrome(head):
                item_dup = self.copy(item)
                item.append(head)
                self.sub_partition(ret, item, tail)
                item = item_dup
        return ret

print Solution().partition("aab")