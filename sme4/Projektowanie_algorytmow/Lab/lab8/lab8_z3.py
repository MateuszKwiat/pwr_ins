class Queue:
    def __init__(self) -> None:
        self.s = []
        self.count = 0

    def push(self, elem):
        self.s.append(elem)
        self.count += 1

    def pop(self):
        if self.count == 0:
            print('queue is already empty')
            return None
        
        temp = self.s[0]        
        self.s.pop(0)
        self.count -= 1
        print(temp)

        return temp

    def clear(self):
        for t in self.s:
            print(t)

        self.s.clear()
        self.count = 0

    def show(self):
        if self.count == 0:
            print('queue is empty')

        for t in self.s:
            print(t)
        print()


queue = Queue()
queue.push(('AUV', 3783.18, 18, 0))
queue.push(('ASV', 9915.03, 86, 1))
queue.push(('AGV', 9042.09, 11, 0))
queue.push(('AUV', 2153.93, 50, 1))
queue.push(('ASV', 5435.13, 93, 0))
queue.push(('ASV', 9115.87, 91, 0))
queue.push(('ASV', 3424.16, 16, 1))
queue.show()

queue.pop()
queue.pop()
queue.pop()
queue.show()

while True:
    val = tuple(input('type, price, range, camera(type exit to stop): ').split(', '))
    if 'exit' in val:
        break

    val = (val[0], float(val[1]), *map(int, val[2:]))
    queue.push(val)
queue.show()

queue.clear()
queue.show()