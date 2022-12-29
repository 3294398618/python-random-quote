import prompt_toolkit


class Node():
    def __init__(self,data=None) -> None:        
        self.data = data
        self.next = None 


class Linked_list():
    def __init__(self) -> None:
         self.head = None

    def Print_list(self):
        prt = self.head
        while prt:
            print(prt.data)
            prt = prt.next
  
    def ending(self,newdata):
        new_node = Node(newdata)
        
        if self.head == None:
            self.head = new_node
            return
            
        last_prt = self.head    
        while last_prt.next:
            last_prt = last_prt.next
        last_prt.next = new_node
    
    def beging(self,newdata):
        new_node = Node(newdata)
        new_node.next = self.head
        self.head = new_node

    def between(self,newdata, prt_node = None):
        new_node = Node(newdata)
        if prt_node == None:
            print("输入一个有效插入点")
            return
        new_node.next = prt_node.next
        prt_node.next = new_node
    
    def del_node(self, dell_key):
        prt = self.head
        if prt:
            if prt.data == dell_key:
                self.head = prt.next
                return
        while prt:
            if prt.data == dell_key:
                break
            qprt = prt
            prt = prt.next
        if prt == None:
            return
        qprt.next = prt.next

link = Linked_list()
link.ending(5)
link.ending(15)
link.ending(25)
link.Print_list()
print("新的链表")
link.del_node(15)
link.Print_list()