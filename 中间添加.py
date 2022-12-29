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

    def between(self, newdata , pre_node = None):
        if pre_node == None:
            print("缺一个插入节点")
            return
        new_node = Node(newdata)
        new_node.next = pre_node.next
        pre_node.next = new_node

    
link = Linked_list()
link.head = Node(5)
n2 = Node(15)
n3 = Node(25)
link.head.next = n2
n2.next = n3
link.print_list()
print("新的链表")
link.between(100, n2)
link.print_list()