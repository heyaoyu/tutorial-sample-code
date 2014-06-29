# https://oj.leetcode.com/problems/remove-duplicates-from-sorted-array/
# del(), pop(), or remove() are not allowed.

# shit!!!, without the answer of https://oj.leetcode.com/discuss/5074/whats-the-valid-format-for-output-python
# only God know how to resolve this problem...

class Solution:
    # @param a list of integers
    # @return an integer
    def removeDuplicates(self, A):
        if A:
            cur = A[0]
            i = 1
            for ele in A[1:]:
                if ele != cur:
                    A[i] = ele
                    i += 1
                    cur = ele
            return i
        else:
            return 0

A = [1,1]
print Solution().removeDuplicates(A)
print A