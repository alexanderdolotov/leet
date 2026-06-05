

'''
155. Min Stack
Medium
Topics
premium lock iconCompanies
Hint

Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

Implement the MinStack class:

    MinStack() initializes the stack object.
    void push(int val) pushes the element val onto the stack.
    void pop() removes the element on the top of the stack.
    int top() gets the top element of the stack.
    int getMin() retrieves the minimum element in the stack.

You must implement a solution with O(1) time complexity for each function.

 

Example 1:

Input
["MinStack","push","push","push","getMin","pop","top","getMin"]
[[],[-2],[0],[-3],[],[],[],[]]

Output
[null,null,null,null,-3,null,0,-2]

Explanation
MinStack minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.getMin(); // return -3
minStack.pop();
minStack.top();    // return 0
minStack.getMin(); // return -2

 

Constraints:

    -2^31 <= val <= 2^31 - 1
    Methods pop, top and getMin operations will always be called on non-empty stacks.
    At most 3 * 104 calls will be made to push, pop, top, and getMin.

 

'''

class MinStack:

    stack = None
    pointer = -1
    min_pointers = None


    def __init__(self):
        self.stack = []
        self.min_pointers = []

    def push(self, val: int) -> None:
        self.pointer += 1

        if self.pointer == len(self.stack):
            self.stack.append(val)
        else:
            self.stack[self.pointer] = val
        
        if len(self.min_pointers) > 0:
            running_min = self.stack[self.min_pointers[-1]]
            if val < running_min:
                self.min_pointers.append(self.pointer)

        else:
            self.min_pointers.append(self.pointer)



    def pop(self) -> None:
        if self.pointer > -1:
            if len(self.min_pointers) > 0:
                if self.pointer <= self.min_pointers[-1]:
                    self.min_pointers.pop()

            self.pointer -= 1

        
    def top(self) -> int:
        if self.pointer > -1:
            return self.stack[self.pointer]
        else:
            return None
        
    def print(self):
        print(self.pointer, self.stack, self.min_pointers)
        

    def getMin(self) -> int:
        if len(self.min_pointers) > 0 and self.pointer >= 0:
            return self.stack[self.min_pointers[-1]]
        else:
            return None





# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()


m = MinStack()

m.print()
m.push(1)
m.push(2)
print('getMin', m.getMin())
m.push(3)
print('getMin', m.getMin())
m.print()

print('getMin', m.getMin())

m.pop()
print(m.top())

m.print()
m.pop()
m.pop()
m.print()

print(m.top())
print('getMin', m.getMin())
m.push(7)
print('getMin', m.getMin())
m.push(8)
print('getMin', m.getMin())
m.push(2)
print('getMin', m.getMin())
print(m.top())
m.print()


m.pop()
m.pop()
m.pop()
m.print()

m.push(1)
m.print()
m.pop()
m.print()
