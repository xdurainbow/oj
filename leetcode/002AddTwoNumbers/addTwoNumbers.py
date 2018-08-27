# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        c = 0
        value = l1.val + l2.val
        if value >= 10:
            value -= 10
            c = 1
        res = ListNode(value)
        tmp = res
        while l1.next is not None or l2.next is not None:
            if l1.next is None:
                value = c + l2.next.val
                l2 = l2.next
            elif l2.next is None:
                value = c + l1.next.val
                l1 = l1.next
            else:
                value = c + l1.next.val + l2.next.val
                l1 = l1.next
                l2 = l2.next
            if value >= 10:
                value -= 10
                c = 1
            else:
                c = 0
            tmp.next = ListNode(value)
            tmp = tmp.next
        if c == 1:
            tmp.next = ListNode(1)
        return res


def ml(s):
    a = int(s[0])
    ret = ListNode(a)
    tmp = ret
    s = s[1:]
    while len(s) != 0:
        tmp.next = ListNode(int(s[0]))
        tmp = tmp.next
        s = s[1:]
    return ret


if __name__ == "__main__":
    sol = Solution()
    list1 = ml("0")
    list2 = ml("18")
    r = sol.addTwoNumbers(list1, list2)

    while r is not None:
        print r.val
        r = r.next
