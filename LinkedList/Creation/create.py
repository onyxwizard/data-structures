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
    
    def search_element(self,key):
        curr = self
        while curr is not None:
            if curr.data == key:
                return True
            curr = curr.next
        
# Traverse from head
def main():
    head = Node(40)
    head.next = Node(30)
    head.next.next = Node(20)
    head.next.next.next = Node(10)
    
    head.traverse()
    
    # Find the Element
    print(head.search_element(key=30))
    

if __name__ == "__main__":
    main()    