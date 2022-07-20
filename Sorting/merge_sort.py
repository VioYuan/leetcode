# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode

        """
        def merge(left, right):
            #merge two sepearate list together
            l = left
            r = right
            res = ListNode(None)
            tmp = res
            #compare the list one by one
            while(l!=None and r != None):
                if l.val <= r.val:
                    tmp.next = ListNode(l.val)
                    tmp = tmp.next
                    l = l.next
                else:
                    tmp.next = ListNode(r.val)
                    tmp = tmp.next
                    r = r.next
            # deal with the rest
            while r != None:
                tmp.next = ListNode(r.val)
                r = r.next
                tmp = tmp.next
            # deal with the rest
            while l!= None:
                tmp.next = ListNode(l.val)
                l = l.next
                tmp = tmp.next
            return res.next
        #recursive helper
        def helper(head):
            if not head or not head.next:
                return head
            p, q = head, head
            # locte the mid pointer
            while q and q.next:
                q = q.next.next
                p_pre = p
                p = p.next
            p_pre.next = None
            #recursively 
            return merge(helper(head), helper(p))
        return helper(head)

def stringToListNode(input):
    # Generate list from the input
    numbers = json.loads(input)

    # Now convert that list into linked list
    dummyRoot = ListNode(0)
    ptr = dummyRoot
    for number in numbers:
        ptr.next = ListNode(number)
        ptr = ptr.next

    ptr = dummyRoot.next
    return ptr

def listNodeToString(node):
    if not node:
        return "[]"

    result = ""
    while node:
        result += str(node.val) + ", "
        node = node.next
    return "[" + result[:-2] + "]"

def main():
    import sys
    def readlines():
        for line in sys.stdin:
            yield line.strip('\n')
    lines = readlines()
    while True:
        try:
            line = lines.next()
            head = stringToListNode(line)
            
            ret = Solution().sortList(head)

            out = listNodeToString(ret)
            print out
        except StopIteration:
            break

if __name__ == '__main__':
    main()
