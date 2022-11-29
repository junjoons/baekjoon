class Stack():
    def __init__(self):
        self.stack = []
        
    def push(self, data):
        self.stack.append(data)
        
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
        
s1 = Stack()
x = int(input())
for y in range(x):
    val = int(input())
    if val != 0:
        s1.push(val)
    else:
        meaninglessvalue = s1.pop()

result = s1.returnStack()
sum = 0
for r in result:
    sum = sum + int(r)
    
print(sum)
