# a)
runif(5000, 0, 1)

# b)
rnorm(3000, 100, 15)

# c)
hist(runif(5000, 0, 1))
hist(rnorm(3000, 100, 15))

density(runif(5000, 0, 1))
density(rnorm(3000, 100, 15))

plot(density(runif(5000, 0, 1)), lwd = 2, col = "red")
plot(density(rnorm(3000, 100, 15)), lwd = 2, col = "red")
