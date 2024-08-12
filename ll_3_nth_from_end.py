class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

class SLL:
    def __init__(self) -> None:
        self.head = None
    
    def insert(self,data):
        new_node = Node(data)
        if not (self.head):
            self.head = new_node
        else:
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = new_node
        

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
        