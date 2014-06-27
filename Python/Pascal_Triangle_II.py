# https://oj.leetcode.com/problems/pascals-triangle-ii/

class Solution:
    # @return a list of integers
    def getRow(self, rowIndex):
        if rowIndex == 0:
            return [1]
        else:
            ret = []
            sub_row = self.getRow(rowIndex-1)
            ret.append(sub_row[0])
            ret.append(sub_row[len(sub_row)-1])
            for i in range(1, len(sub_row)-2+2):#-2: 0 and len()-1
                ret[i:i] = (sub_row[i-1]+sub_row[i], )
            return ret


def main():
    for i in range(10):
        print Solution().getRow(i)


if __name__=='__main__':
    main()