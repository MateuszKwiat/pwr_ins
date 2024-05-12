class List:
    def __init__(self) -> None:
        self.s = []

    def push(self, elem):
        self.s.append(elem)

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
list.push(('AUV', 3783.18, 0, 0))
list.push(('AUV', 3783.18, 1, 0))
list.push(('ASV', 9915.03, 2, 1))
list.push(('AGV', 9042.09, 3, 0))
list.push(('AUV', 2153.93, 4, 1))
list.push(('ASV', 5435.13, 5, 0))
list.push(('ASV', 9115.87, 6, 0))
list.push(('ASV', 3424.16, 7, 1))
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