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
    
    #Insert a Node at Front/Beginning of a Linked List
    def insert_node_begin(self,new_data):
        #create a new node
        new_node = Node(new_data)
        new_node.next = self
        return new_node

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
        
    #Deletion at the Beginning of Singly Linked List
    def delete_node_begin(self):
        if self is None:
            return "Empty L-List"
        cur = self
        self = self.next
        del cur
        return self

    #Deletion at end (Removal of last node) in a Linked List
    def delete_node_end(self):
        if self is None:
            return "empty list"
        cur = self
        while cur.next.next is not None:
            cur = cur.next
        cur.next = None
        return self
    
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
    
    # Traverse from head
    print(f"\n Traverse the Linked List")
    head.traverse()
    
    # Find the Element
    keys=30
    print(f"\n Find Element {keys} in Linked List")
    print(head.search_element(key=keys))
    
    #Insert at Begin
    print("\n Insert New node at Begin")
    data = 50
    head = head.insert_node_begin(data)
    head.traverse()
    
    #Insert at End
    print("\n Insert New node at End")
    data2 = 1
    head = head.insert_node_end(new_data=data2)
    head.traverse()
    
    #Insertion at a Specific Position 
    print("\n Insert New node at Specific Position")
    position = 2
    data3 = 45
    head = head.insert_node_at_pos(new_data=data3,pos=position)
    head.traverse()
    
    #Delete at Begin
    print("\n Delete node at Begin")
    head = head.delete_node_begin()
    head.traverse()
    
    #Delete at End
    print("\n Delete node at End")
    head = head.delete_node_end()
    head.traverse()
    
    #Delete at Specific Position
    print("\n Delete node at Specific Position")
    pos = 2
    head = head.delete_node_pos(pos)
    head.traverse()
        
if __name__ == "__main__":
    main()    