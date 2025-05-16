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
    
    #Insertion at a Specific Position 
    def insert_node_at_pos(self,new_data,pos):
        cur = self
        count = 0
        new_node = Node(new_data)
        while cur is not None and count < pos-1:
            cur = cur.next
            count+=1
        if cur is None:
            print("Position out of bounds")
            return self
        
        new_node.next = cur.next
        cur.next = new_node
        return self

def main():
    head = Node(40)
    head.next = Node(30)
    head.next.next = Node(20)
    head.next.next.next = Node(10)
    
    #Insertion at a Specific Position 
    print("\n Insert New node at Specific Position")
    position = 2
    data3 = 45
    head = head.insert_node_at_pos(new_data=data3,pos=position)
    head.traverse()

if __name__ == "__main__":
    main()    