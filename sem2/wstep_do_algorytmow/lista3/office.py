from sinlgyLinkedList import SinglyLinkedList
from sinlgyLinkedList import Node
from random import randint

class Office:
    def __init__(self, numOfCounters, ranges, countersTypeE, size):
        self.counter = [0]*numOfCounters
        self.customerCountPerCounter = [0]*numOfCounters
        self.ranges = ranges
        self.counterTypeE = countersTypeE
        self.customers = SinglyLinkedList()
        self.customer = None
        for x in range(0, size):
            self.customers.insertHead(Node(randint(1, 12)))


    def timeCount(self):
        time = 0
        maxVal = 0
        startSim = True

        while startSim == True or maxVal != 0:
            startSim = False
            for i in range(0, len(self.counter)):
                if self.counter[i] > 0:
                    self.counter[i] -= 1

            if not self.customers.isEmpty():
                # for A
                if self.customers.head.data in range(1, 5):
                    for i in range(self.ranges[0], self.ranges[1]):
                        self.checkForNewCust(i)
                # for B
                elif self.customers.head.data in range(5, 9):
                    for i in range(self.ranges[1], self.ranges[2]):
                        self.checkForNewCust(i)
                # for C
                elif self.customers.head.data in range(9, 13):
                    for i in range(self.ranges[2], self.ranges[3]):
                        self.checkForNewCust(i)
                # for E
                if self.counterTypeE == True:
                    for i in range(self.ranges[3], self.ranges[4]):
                        self.checkForNewCust(len(self.counter) - 1)

            time += 1

            ## DEBUG
            #print(f"time: {time}")
            #for i in range(0, 10):
            #    print(f"{i}: {self.counter[i]}")
            #print(f"cust: {self.customer.data}")
            #print()

            maxVal = max(self.counter)
            self.customer = Node(0)

        # RESULTS
        print(f"Iterations: {time}")
        for i in range(0, len(self.counter)):
            print(f"counter {i}: {self.customerCountPerCounter[i]}")
        print()

    def checkForNewCust(self, i):
        if self.counter[i] == 0 and not self.customers.isEmpty():
            self.customer = self.customers.removeHead()
            self.counter[i] += self.customer.data
            self.customerCountPerCounter[i] += 1


    # DEBUG
    def showCustomers(self):
        while not self.customers.isEmpty():
            print(f"remove head: {self.customers.removeHead()}")
        


    