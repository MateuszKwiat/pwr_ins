class List:
    def __init__(self) -> None:
        self.s = []

    def push(self, ind, elem):
        self.s.insert(ind, elem)

    def pop(self, ind):
        if len(self.s) == 0:
            print('list is already empty')
            return None
        

        temp, i = self.find_elem(ind)        
        self.s.pop(i)
        print(temp)

        return temp
    
    def find_elem(self, ind):
        if ind[0] == 'X' and len(ind) >= 2:
            for i in ind[1:]:
                if i != 'D':
                    print('indexing error: incorrect foramt')
                    return None
            print(self.s[len(ind[1:]) - 1])
            return self.s[len(ind[1:]) - 1], len(ind[1:]) - 1
        
        print('indexing error: incorrect foramt')
        return None
        
    def show(self):
        if len(self.s) == 0:
            print('list is empty')

        for t in self.s:
            print(t)
        print()

list = List()
list.push(0, ('AUV', 3783.18, 0, 0))
list.push(1, ('AUV', 3783.18, 1, 0))
list.push(2, ('ASV', 9915.03, 2, 1))
list.push(3, ('AGV', 9042.09, 3, 0))
list.push(4, ('AUV', 2153.93, 4, 1))
list.push(5, ('ASV', 5435.13, 5, 0))
list.push(6, ('ASV', 9115.87, 6, 0))
list.push(7, ('ASV', 3424.16, 7, 1))
list.show()

list.pop('XDDD')
list.pop('XD')
list.pop('XDD')
print()
list.show()

print()
list.find_elem('XDD')
list.find_elem('XDDD')
list.find_elem('XDDDD')
list.find_elem('XD')

list.push(2, ('ASV', 3424.16, 15, 1))
print()
list.show()