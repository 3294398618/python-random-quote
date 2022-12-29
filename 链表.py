class Node:
    # 节点
    def __init__(self, data=None):
        self.data = data
        self.next = None


class Linked_list:
    def __init__(self):
        self.head = None

    def print_list(self):
        # 打印链表

        ptr = self.head
        while ptr:
            print(ptr.data)
            ptr = ptr.next


link = Linked_list()
link.head = Node(5)
n2 = Node(15)
n3 = Node(20)
link.head.next = n2
n2.next = n3

link.print_list()
