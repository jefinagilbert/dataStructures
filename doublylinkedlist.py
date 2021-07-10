class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList:

    def __init__(self):
        self.head = None

    def append(self,new_data):
        new_node = Node(new_data)
        if self.head is None:
            self.head = new_node
            return 
        last = self.head
        while last.next:
            last.next = last
        last.next = new_node
        new_node.prev = last
        return

    def push(self,new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        if self.head is not None:
            self.head.prev = new_node
        self.head = new_node

    def printList(self, node):
 
        print("\nNext Nodes")
        while node:
            print(node.data)
            last = node
            node = node.next
 
        print("\nPrevious Nodes")
        while last:
            print(last.data)
            last = last.prev
 
llist = DoublyLinkedList()
llist.append(6)
llist.append(4)
llist.push(10)
print("Created DLL is: ")
llist.printList(llist.head)