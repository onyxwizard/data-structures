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
        
    #Reverse a Linked List
    def reversal_linked_list(self):
        prev = None
        curr = self
        next_node = None
        
        while curr is not None:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
            
        return prev
            
    
def main():
    head = Node(40)
    head.next = Node(30)
    head.next.next = Node(20)
    head.next.next.next = Node(10)
    
    # Reverse from head
    print(f"\n Reverse the Linked List")
    head = head.reversal_linked_list()
    head.traverse()


if __name__ == "__main__":
    main()    