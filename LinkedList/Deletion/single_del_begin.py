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
            
    #Deletion at the Beginning of Singly Linked List
    def delete_node_begin(self):
        if self is None:
            return "Empty L-List"
        cur = self
        self = self.next
        del cur
        return self

def main():
    head = Node(40)
    head.next = Node(30)
    head.next.next = Node(20)
    head.next.next.next = Node(10)
    
    #Delete at Begin
    print("\n Delete node at Begin")
    head = head.delete_node_begin()
    head.traverse()
    
if __name__ == "__main__":
    main()    