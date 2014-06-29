# https://oj.leetcode.com/problems/string-to-integer-atoi/

# char.isdigit() !!!!!
# str.strip() == trim() !!!!!

class Solution:

    # @return an integer
    def atoi(self, str):
        str = str.strip()
        if str=="":
            return 0
        minus = 1
        if str[0] == '-':
            minus = -1
            str = str[1:]
        elif str[0] == '+':
            str = str[1:]
        ret = 0
        for i in range(len(str)):
            char = str[i]
            if char.isdigit():
                ret *= 10
                ret += ord(char)-ord('0')
            else:
                ret = minus*ret
                if ret>2147483647:
                    return 2147483647
                elif ret<-2147483648:
                    return -2147483648
                else:
                    return ret
        ret = minus*ret
        if ret>2147483647:
            return 2147483647
        elif ret<-2147483648:
            return -2147483648
        else:
            return ret

print Solution().atoi("-1")