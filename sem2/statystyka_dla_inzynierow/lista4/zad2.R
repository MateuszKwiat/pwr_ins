# a)
diceThrows <- floor(runif(600, 0, 6)) + 1
mean(diceThrows)
3.5 - mean(diceThrows)

var(diceThrows)
35/12 - var(diceThrows)

# b)
tab <- table(diceThrows)
for (x in tab) {
  print(x - 100)
}

tabAsDf <- as.data.frame(tab)
tabAsDf
var(tabAsDf["Freq"])

# c)
diceThrows1 <- sample(c(1:6), 600, TRUE, c(1/6, 1/6, 1/6, 1/6, 1/6, 1/6))
mean(diceThrows1)
var(diceThrows1)
as.data.frame(table(diceThrows1))

