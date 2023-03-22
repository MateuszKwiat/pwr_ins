# a)
x <- 0:100
plot(dbinom(x, 100, .02), type = "h")
lines(x, dpois(x, 2), type = "l", col = "red")

