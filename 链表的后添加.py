class Node():
    def __init__(self,data=None) -> None:
        self.data = data 
        self.next = None


class Linked_list():
    def __init__(self) -> None:
        self.head = None

    def print_list(self):
        prt = self.head
        while prt:
            print(prt.data)
            prt = prt.next
    
    def ending(self,newdata):
        new_node = Node(newdata)
        if self.head == None:
            self.head == new_node
            return
        last_prt = self.head
        while last_prt.next:
            last_prt = last_prt.next
        last_prt.next = new_node



link = Linked_list()
link.head = Node(5)
n2 = Node(15)
n3 = Node(25)
link.head.next = n2
n2.next = n3
link.print_list()
print("新的链表")
link.ending(100)
link.print_list()