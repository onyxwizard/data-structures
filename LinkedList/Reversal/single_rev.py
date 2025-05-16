# Creating a LinkedList 
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
    
    # Traversal in a linked list means visiting each node and performing operations like printing or processing data.
    def traverse(self):
        # 'current' starts at the node we called traverse() on
        current = self  # Start traversal from current node
        while current is not None:
            print(current.data)
            current = current.next  # Move to next node
            
    def reversal_stack(self):
        stack = []
        cur = self
        # Push all nodes except last one into the stack
        while cur.next is not None:
            stack.append(cur)
            cur = cur.next
        
        # Now cur is at the last node (new head)
        new_head = cur
        while stack:
            cur.next = stack.pop()
            cur = cur.next
        cur.next = None  # Final node (was head) now points to None

        return new_head

    def reverse_pointers(self):
        prev = None
        curr = self
        while curr is not None:
            next_node = curr.next  # Save next node before breaking link
            curr.next = prev       # Reverse link
            prev = curr            # Move prev forward
            curr = next_node       # Move curr forward
        return prev  # prev is now the new head
    
    
def main():
    head = Node(40)
    head.next = Node(30)
    head.next.next = Node(20)
    head.next.next.next = Node(10)
    
    # Reverse from head
    print(f"\n Reverse the Linked List using Pointers")
    head = head.reverse_pointers()
    head.traverse()
    
    # Reverse from head
    print(f"\n Reverse the Linked List using Stack")
    head = head.reversal_stack()
    head.traverse()
    


if __name__ == "__main__":
    main()    