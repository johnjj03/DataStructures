class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

def nth_from_end(head, n):
    dummy = Node(0,head)
    left = dummy
    right = head

    while (n>0):
        right = right.next
        n-=1
    
    while right:
        right = right.next
        left = left.next 
    left.next = left.next.next
    return dummy.next
        