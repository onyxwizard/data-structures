# Creating a LinkedList 
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
    
def main():
    head = Node(40)
    head.next = Node(30)
    head.next.next = Node(20)
    head.next.next.next = Node(10)
    
    #print Node
    print(f'Output Head Node which gives : {head}\nNow lets output its data:\n {head.data} -> {(head.next).data} -> {(head.next.next).data} -> {(head.next.next.next).data} ')
    
        
if __name__ == "__main__":
    main()    