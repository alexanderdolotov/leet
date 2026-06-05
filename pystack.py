

'''

 

'''

class Stack:

    stack = []
    pointer = -1

    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        self.pointer += 1

        if self.pointer == len(self.stack):
            self.stack.append(val)
        else:
            self.stack[self.pointer] = val
        

    def pop(self) -> None:
        if self.pointer > -1:
            self.pointer -= 1
        
    def top(self) -> int:
        if self.pointer > -1:
            return self.stack[self.pointer]
        else:
            return None
        
    def print(self):
        print(self.pointer, self.stack)




m = Stack()

m.print()
m.push(1)
m.push(2)
m.push(3)
m.print()

m.pop()
print(m.top())

m.print()
m.pop()
m.pop()
m.print()

print(m.top())
m.push(7)
m.push(8)
m.push(9)
print(m.top())
m.print()

