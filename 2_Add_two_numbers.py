class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1, l2):
        # carry represents the carry that needs to be added to the next digits in the sum of the two linked lists.
        carry = 0
        # create empty node, this will serve as the head of the linked list that we will returned
        head = ListNode()
        # use this variable to traverse the linked list that we will create and add new nodes to it.
        current = head

        # Loop through both linked lists until either one becomes None. 
        # We will add the digits of the two linked lists along with the carry 
        # value and create new nodes to store the sum in the output linked list.
        while(l1 and l2):
            # sum of the current nodes in l1 and l2, as well as the carry value from the previous iteration.
            sum = l1.val + l2.val + carry
            # calculate the new carry
            carry = int(sum / 10)
            # create a new ListNode object and append it to the end of the current list.
            current.next = ListNode(sum % 10) 
            # Move current, l1, and l2 to point to the next nodes in their respective lists.
            current, l1, l2 = current.next, l1.next, l2.next
        
        # check if there are still nodes in l1.
        # loop through and add them to the output linked list.
        while(l1):
            sum = l1.val + carry
            carry = int(sum / 10)
            current.next = ListNode(sum % 10)
            current, l1 = current.next, l1.next
        
        # do the same for l2
        while(l2):
            sum = l2.val + carry
            carry = int(sum / 10)
            current.next = ListNode(sum % 10)
            current, l2 = current.next, l2.next
        
        # If there is still a carry value, create a new ListNode object 
        # with a value of 1 and append it to the end of the current list.
        if carry == 1:
            current.next = ListNode(1)

        # skip the head because head is an empty node.
        return head.next

def p_ll(ll):
    while ll:
        print(ll.val)
        ll = ll.next

l1n3 = ListNode(9)
l1n2 = ListNode(9, l1n3)
l1n1 = ListNode(9, l1n2)
l1 = l1n1

l2n3 = ListNode(9)
l2n2 = ListNode(9, l2n3)
l2n1 = ListNode(9, l2n2)
l2 = l2n1

ans = Solution()
#print(l1.val)
p_ll(ans.addTwoNumbers(l1, l2))
