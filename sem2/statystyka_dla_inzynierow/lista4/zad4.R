# a)
coinTosses <- sample(c(0:1), 100, TRUE, c(1/2, 1/2))
for (x in c(1:100)) {
  print(dbinom(coinTosses[x], 10, 0.3))
}

# b)
for (x in c(1:50)) {
  print(dgeom(coinTosses[x], 0.4))
}