# https://oj.leetcode.com/problems/sort-list/

# Definition for singly-linked list.
# class ListNode:
#      def __init__(self, x):
#          self.val = x
#          self.next = None

class Solution:
    # @param head, a ListNode
    # @return a ListNode
    def sortList(self, head):
        if head is None:
            return None
        length = self.len_List(head)
        if length == 1:
            return head
        h = head
        t = head
        tmp = None
        for i in range(length/2):
            tmp = t
            t = t.next
        tmp.next = None
        new_h = self.sortList(h)
        new_t = self.sortList(t)
        ret = self.merge(new_h, new_t)
        return ret

    def merge(self, h, t):
        if h is None:
            return t
        if t is None:
            return h
        ret = None
        tail = None
        while h and t:
            if h.val<t.val:
                if ret:
                    tail.next = h
                    tail = h
                    h = h.next
                    tail.next = None
                else:
                    ret = h
                    h = h.next
                    ret.next = None
                    tail = ret
            else:
                if ret:
                    tail.next = t
                    tail = t
                    t = t.next
                    tail.next = None
                else:
                    ret = t
                    t = t.next
                    ret.next = None
                    tail = ret
        while h:
            tail.next = h
            break
        while t:
            tail.next = t
            break
        return ret


    def len_List(self, head):
        if head is None:
            return 0
        length = 1
        while head.next is not None:
            length += 1
            head = head.next
        return length