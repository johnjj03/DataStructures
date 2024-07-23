class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

def remove_duplicates(head):
    current = head
    while current and current.next:
        if current.data == current.next.data:
            current.next = current.next.next
        else:
            current = current.next
    return head
