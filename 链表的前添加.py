class Node():
    # 节点
    def __init__(self,data=None) -> None:
        self.data = data
        self.next = None

class Linked_list():
    # 链表主体
    def __init__(self) -> None:
        self.head = None
    
    def print_list(self):
        # 打印链表
        ptr = self.head
        while ptr:
            print(ptr.data)
            ptr = ptr.next
    
    def begining(self,newdata):
        # 插入节点
        new_node = Node(newdata)
        new_node.next = self.head
        self.head = new_node


link = Linked_list()
link.head = Node(5)
n2 = Node(15)
n3 = Node(25)
link.head = n2
n2.next = n3 
link.print_list()
print("新的链表")
link.begining(100)
link.print_list()