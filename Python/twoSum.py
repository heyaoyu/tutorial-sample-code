class Solution:
    # @return a tuple, (index1, index2)
    def twoSum(self, num, target):
        hash = {}
        for i in range(len(num)):
            left = target - num[i]
            if hash.get(left, -1)!=-1:
                return (i+1, hash.get(left)+1) if i<hash.get(left) else (hash.get(left)+1, i+1)
            if num[i]<=target:
                hash[num[i]] = i

print Solution().twoSum([0,2,4,0], 0)