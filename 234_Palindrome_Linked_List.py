# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def print_list(self, head):
            current = head

            while current != None:
                print(current.val, end = ' ')
                current = current.next
            print('')

    # Split the linked list in half and reverse the second half
    # compare the first half and second half
    def isPalindrome(self, head: ListNode) -> bool:
        def reverse(header):
            prev = None
            current = header
            
            while current is not None:
                next = current.next
                current.next = prev
                prev = current
                current = next

            return prev
        
        # slow, fast pointer to get the middle of linked list
        slow = head
        fast = head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # revese list starting from slow.next
        h1 = head
        h2 = reverse(slow.next) # root of second half of the reversed list
        while h2:
            if h1.val != h2.val:
                return False

            h1 = h1.next
            h2 = h2.next

        return True

node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(2)
node4 = ListNode(1)
node5 = ListNode(1)

head = node1
node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5

ans = Solution()
ans.print_list(head)
print(ans.isPalindrome(head))
