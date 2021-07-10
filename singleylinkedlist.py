class node:
    def __init__(self,data):
        self.data = data
        self.next = None
    

class linkedlist:
    def __init__(self):
        self.head = None


    def printlinkedlist(self):
        temp = self.head
        print (temp)
        while (temp):
            print (temp.data,end=" -> ")
            temp = temp.next 
    

    def append(self, new_data): 
        
        new_node = node(new_data) 

        if self.head is None: 
            self.head = new_node 
            return

        last = self.head 
        while (last.next): 
            last = last.next
            
        last.next =  new_node 

    def push(self, new_data): 
        new_node = node(new_data) 
        new_node.next = self.head 
        self.head = new_node 

    def insertAfter(self, prev_node, new_data): 
  
        if prev_node is None: 
            print("The given previous node not inLinkedList.")
            return

        new_node = node(new_data) 
  
        new_node.next = prev_node.next
  
        prev_node.next = new_node 


    def deletenode(self,key):
        temp = self.head
        if (temp is not None):
            if key == temp.data:
                self.head = temp.next
                temp = None

        while (temp is not None):
            if temp.data == key:
                break
            prev = temp
            temp = temp.next
        if (temp is None):
            return
        prev.next = temp.next
        temp = None


    def deletelist(self):
        temp = self.head   #  we can also use Only self.head = None
        while (temp):
            next = temp.next
            del temp.data
            temp = next
        self.head = None

    def deletenodeposition(self,position):
        temp = self.head
        if (self.head is None):
            return
        if position == 0:
            self.head = temp.next
            temp = None
            return
        for i in range(position - 1):
            temp = temp.next
            if (temp is None):
                break
        if (temp is None):
            return
        if (temp.next is None):
            return
        next = temp.next.next
        temp.next  = None
        temp.next = next



if __name__ == "__main__":
    llist = linkedlist()

    while True:
        print()
        print("------ NOTES ------")
        print()
        print("1. Append Value")
        print()
        print("2. Push Value")
        print()
        print("3. Insert After")
        print()
        print("4. Display Node")
        print()
        print("5. Delete Node by data")
        print()
        print("6. Delete Node by Position")
        print()
        print("7. Delete Linked list")
        print()
        print("8. Exit")
        i = int(input("Enter the Number: "))
        if i == 1:
            k = int(input("enter value to append : "))
            llist.append(k)
            print()
            print(k," Appended Successfully")  
        elif i == 2:
            k = int(input("enter value to push : "))
            llist.push(k)
        elif i == 3:
            k = int(input("enter value to add after : "))
            llist.insertAfter(llist.head.next,k)
        elif i == 4:
            llist.printlinkedlist()
        elif i == 5:
            k = int(input("enter value to deletenode : "))
            llist.deletenode(k)
        elif i == 6:
            k = int(input("enter position to Delete : "))
            llist.deletenodeposition(k)
        elif i == 7:
            llist.deletelist()
        elif i == 8:
            break
        else:
            print("Enter Valid Number")

