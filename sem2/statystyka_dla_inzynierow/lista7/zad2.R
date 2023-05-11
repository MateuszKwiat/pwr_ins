# a)
n <- 10000

u1 <- runif(n)
u2 <- runif(n)

z <- cos(2*pi*u1) * sqrt(-2*log(u2))

hist(z, breaks = 30, xlab = "Z")

# b)
x <- seq(min(z), max(z), length.out = 1000)

dens <- density(z, bw = "nrd")

plot(dens, xlab = "Z", ylab = "density", ylim = c(0, 0.45))

lines(x, dnorm(x), col = "red")

# c)
Y <- 100 + 15*z

x <- seq(min(Y), max(Y), length.out = 1000)

dens <- density(Y, bw = "nrd")

plot(dens, xlab = "Y", ylab = "density", ylim = c(0, 0.015))

lines(x, dnorm(x, mean = 100, sd = 15), col = "red")
