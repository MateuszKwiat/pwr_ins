
class Stack:
    def __init__(self) -> None:
        self.s = []
        self.i = -1

    def push(self, elem):
        self.s.append(elem)
        self.i += 1

    def pop(self):
        temp = self.s[self.i]
        self.s.pop(self.i)
        self.i -= 1

        return temp

    def clear(self):
        for t in self.s[::-1]:
            print(t)

        self.s.clear()
        i = -1

    def show(self):
        if len(self.s) == 0:
            print('stack is empty')

        for t in self.s[::-1]:
            print(t)
        print()

stack = Stack()
stack.push(('AUV', 3783.18, 18, 0))
stack.push(('ASV', 9915.03, 86, 1))
stack.push(('AGV', 9042.09, 11, 0))
stack.push(('AUV', 2153.93, 50, 1))
stack.push(('ASV', 5435.13, 93, 0))
stack.push(('ASV', 9115.87, 91, 0))
stack.push(('ASV', 3424.16, 16, 1))
stack.show()

stack.pop()
stack.pop()
stack.pop()
stack.show()

while True:
    val = tuple(input('type, price, range, camera(type exit to stop): ').split(', '))
    if 'exit' in val:
        break

    val = (val[0], float(val[1]), *map(int, val[2:]))
    stack.push(val)
stack.show()

stack.clear()
stack.show()