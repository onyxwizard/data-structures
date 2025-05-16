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
            
    #Deletion at end (Removal of last node) in a Linked List
    def delete_node_end(self):
        if self is None:
            return "empty list"
        cur = self
        while cur.next.next is not None:
            cur = cur.next
        cur.next = None
        return self
    

def main():
    head = Node(40)
    head.next = Node(30)
    head.next.next = Node(20)
    head.next.next.next = Node(10)   
    
    #Delete at End
    print("\n Delete node at End")
    head = head.delete_node_end()
    head.traverse()
    
if __name__ == "__main__":
    main()    