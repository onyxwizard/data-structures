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
            
    #Deletion at Specific Position in a Linked List
    def delete_node_pos(self,pos):
        if self is None:
            return "empty list"
        
        # Case 1: Delete head node (position 0)
        if pos == 0:
            return self.next
        
        cur = self
        count = 0
        while cur is not None and count<pos-1:
            cur = cur.next
            count+=1
        # Check if cur or cur.next is None (i.e., pos is out of bounds)
        if cur is None or cur.next is None:
            print("Position out of bounds")
            return self
        
        cur.next = cur.next.next
        return self
    

def main():
    head = Node(40)
    head.next = Node(30)
    head.next.next = Node(20)
    head.next.next.next = Node(10)   
    
    #Delete at Specific Position
    print("\n Delete node at Specific Position")
    pos = 2
    head = head.delete_node_pos(pos)
    head.traverse()
    
if __name__ == "__main__":
    main()    