import numpy as np

class ReceiptChecker:
    def __init__(self, m, n):
        self.rowsClient = m
        self.rowsProducts = n
        self.clientReceipt = np.zeros((self.rowsClient, 3), dtype=float)
        self.productsData = np.full((self.rowsProducts, 4), "", dtype=object)

        self.fill()
        print(self.clientReceipt)
        print(self.productsData)

    
    def fill(self):
        choice = int(input("Czy uzupelnic danymi z \"scenariusz testowy\"? <1 - tak, 0 - nie>"))

        if choice == 1:
            self.clientReceipt = np.array([[3, 2, 4],
                                           [3, 1, 1],
                                           [3, 5, 0.3],
                                           [3, 4, 6]])
            self.productsData = np.array([[1, 50, "szt.", "suszarka el."],
                                          [2, 2.98, "waga", "jablka"],
                                          [3, 7, "waga", "pomarancze"],
                                          [4, 4, "szt.", "szklanka"],
                                          [5, 32, "waga", "szynka"]])    
        else:
            print("Paragon klienta:")
            for i in range(0, self.rowsClient):
                for j in range(0, 3):
                    self.clientReceipt[i][j] = float(input(f"clientReceipt[{i}][{j}]: "))

            self.productsData.reshape(self.rowsProducts, 4)
            for i in range(0, self.rowsProducts):
                for j in range(0, 4):
                    self.productsData[i][j] = str(input(f"productsData[{i}][{j}]: "))

    
    def checkIfReceiptIsCorrect(self):
        inProductData = False
        notAnInt = False

        for i in range(0, self.rowsClient):
            for j in range(0, self.rowsProducts):
                # czy numer towaru jest na liscie
                if self.clientReceipt[i][1] == int(self.productsData[j][0]):
                    inProductData = True
                    # czy towar na sztuki jest liczba calkowita
                    if self.productsData[j][2] == "szt." and self.clientReceipt[i][2] % 1 != 0:
                        notAnInt = True
                
            if inProductData == False:
                print("Nie znaleziono produktu na liscie towarow.")
                quit()

            if notAnInt == True:
                print("Towar na sztuki nie jest liczba calkowita.")
                quit()

            inProductData = False


    def calculatePrice(self):
        price = 0

        for i in range(0, self.rowsClient):
            for j in range(0, self.rowsProducts):
                if self.clientReceipt[i][1] == int(self.productsData[j][0]):
                    price = price + self.clientReceipt[i][2] * float(self.productsData[j][1])

        return price

m = int(input("Liczba kolumn na paragonie\n>"))
n = int(input("Liczba kolumn na liscie towarow\n>"))
zad4obj = ReceiptChecker(m, n)
zad4obj.checkIfReceiptIsCorrect()
print(zad4obj.calculatePrice())