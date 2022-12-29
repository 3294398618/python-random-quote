
class Stack():
    def __init__(self) -> None:
        self.my_stack = []
    
    def my_append(self,data):
        self.my_stack.append(data)
    
    def my_pop(self):
        return self.my_stack.pop()

    def size(self):
        return len(self.my_stack)
    # 判断是否为空列表  
    def isEmpty(self):
        return self.my_stack == []

stack = Stack()
fruits = ['Grape','Mango','Apple']
for fruit in fruits:
    stack.my_append(fruit)
    print('被推入的水果有',fruit) 

print(f'栈有{stack.size()}种水果')
# 全部推出去
while not stack.isEmpty():
    print(stack.my_pop())
