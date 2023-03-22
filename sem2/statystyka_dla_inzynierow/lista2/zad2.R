# a)
# sr tyg = 3
# X = l. sprz przez 2 tyg
# w 2 tyg 2 * 3 = 6
# X ~ Poisson(6)
dpois(5, 6)

# b)
1 - ppois(3, 6)

# c)
ppois(5, 6) - ppois(2, 6)

# d)
x <- 0:30;
plot(x, dpois(x, 6), type = "h")
