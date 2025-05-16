# Creating a LinkedList 
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def search_element(self,key):
        curr = self
        while curr is not None:
            if curr.data == key:
                return True
            curr = curr.next
    
def main():
    head = Node(40)
    head.next = Node(30)
    head.next.next = Node(20)
    head.next.next.next = Node(10)
        
    # Find the Element
    keys=30
    print(f"\n Find Element {keys} in Linked List")
    print(head.search_element(key=keys))


if __name__ == "__main__":
    main()    