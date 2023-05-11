# a)
x <- rnorm(2000, mean = 170, sd = 12)
x

# b)
Z <- (x - 170) / 12
es <- density(Z)
plot(es, xlim = c(-4, 4))
curve(dnorm(x), from = -4, to = 4, add = TRUE, col = "red")
