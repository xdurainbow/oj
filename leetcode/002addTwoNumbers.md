# 题目描述
You are given two **non-empty** linked lists representing two non-negative integers. The digits are stored in **reverse order** and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

**Example**

	Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
	Output: 7 -> 0 -> 8
	Explanation: 342 + 465 = 807.

# 题目解析
逆序给出两个非空的linked list，每一位都是一个非负个位数，链表逐位相加，返回结果依然是一个链表

# 解题
遍历两个链表，逐位相加，设置一个进位标记，每次相加有进位时，该标记赋值为1，否则为0。

1.  利用一个**while循环**来遍历链表，直至两个输入链表都为空
2. 每次检查两个链表中是否存在为空的，如果为空，则输出链表中该位的值有进位值加上另一个链表在该位的值
3. 当一个链表为空时，该链表不再向后取next，否则计算完之后，链表向后移一位
4. 没一位计算结束之后，再次计算进位值
5. 整体循环结束之后，再次判断是否有进位

# 完整代码
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
