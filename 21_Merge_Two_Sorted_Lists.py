#Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: ListNode, list2: ListNode) -> ListNode:
        current = out = ListNode()

        # compare the values and merge into a single list
        while list1 and list2:
            if list1.val < list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next
            
            current = current.next

        # append the remaining elements of list1 or list2
        if list1 or list2:
            current.next = list1 if list1 else list2 
        
        return out.next

list1 = ListNode(1)
l12 = ListNode(2)
l13 = ListNode(4)

list2 = ListNode(2)
l22 = ListNode(3)
l23 = ListNode(4)

list1.next = l12
list1.next.next = l13

list2.next = l22
list2.next.next = l23

# print(list1.val)
# print(list1.next.val)
# print(list1.next.next.val)

a = Solution()
out = a.mergeTwoLists(None, None)
print(out)
