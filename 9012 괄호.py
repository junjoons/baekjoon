class Stack():
    def __init__(self):
        self.stack = []
        self.opened = 0
        self.result = "NULL"
        
    def push(self, data):
        self.stack.append(data)
        if data == ")":
            if self.isOpened() == 0:
                self.result = "NO"
            else:
                self.opened = self.opened - 1
        elif data == "(":
            self.opened = self.opened + 1
        
    def pop(self):
        pop_object = None
        if self.isEmpty():
            print("Stack is Empty")
        else:
            pop_object = self.stack.pop()
            
        return pop_object
            
    def top(self):
        top_object = None
        if self.isEmpty():
            print("Stack is Empty")
        else:
            top_object = self.stack[-1]
            
        return top_object
            
            
    def isEmpty(self):
        is_empty = False
        if len(self.stack) == 0:
            is_empty = True
        return is_empty
    
    def returnStack(self):
        return self.stack

    def isOpened(self):
        return self.opened

    def result(self):
        if self.result == "NO" or self.result == "NULL" or self.result<0:
            return "NO"
        else: return "YES"

        
s1 = Stack()
x = int(input())
for y in range(x):
    val = input()
    for z in val:
        s1.push(z)
        if s1.result() == "NO":
            print("NO")
            break
        

print(s1.result())
    
