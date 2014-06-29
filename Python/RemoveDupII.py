# https://oj.leetcode.com/problems/remove-duplicates-from-sorted-array-ii/
class Solution:
    # @param A a list of integers
    # @return an integer
    def removeDuplicates(self, A):
        k = 2
        if len(A) <= k:
            return len(A)
        j = 0
        cur = A[j]
        i = k
        for ele in A[k:]:
            if ele!=cur:
                A[i] = ele
                i += 1
                j += 1
                cur = A[j]
        return i

A = [1,1,2,2]
print Solution().removeDuplicates(A)
print A