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
    
    #Insert a Node at End of a Linked List
    def insert_node_end(self,new_data):
        #create a new node
        new_node = Node(new_data)
        cur = self
        while cur.next is not None:
            cur = cur.next
        cur.next = new_node
        new_node.next = None
        return self


def main():
    head = Node(40)
    head.next = Node(30)
    head.next.next = Node(20)
    head.next.next.next = Node(10)

    #Insert at End
    print("\n Insert New node at End")
    data2 = 1
    head = head.insert_node_end(new_data=data2)
    head.traverse()
    

if __name__ == "__main__":
    main()    