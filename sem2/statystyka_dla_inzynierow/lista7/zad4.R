# a)
s_1 <- sum(rexp(1000, rate = 0.5))
s_20 <- sum(rexp(1000 * 20, rate = 0.5))
s_200 <- sum(rexp(1000 * 200, rate = 0.5))

z_1 <- (s_1 - 2) / sqrt(2)
z_20 <- (s_20 - 40) / sqrt(40)
z_200 <- (s_200 - 400) / sqrt(400)

cat(sprintf("S_1 = %.2f, Z_1 = %.2f\n", s_1, z_1))
cat(sprintf("S_20 = %.2f, Z_20 = %.2f\n", s_20, z_20))
cat(sprintf("S_200 = %.2f, Z_200 = %.2f\n", s_200, z_200))

# b)
z_1 <- rnorm(1000, mean = 0, sd = 1)
z_20 <- rnorm(1000 * 20, mean = 0, sd = 1)
z_200 <- rnorm(1000 * 200, mean = 0, sd = 1)

dens_1 <- density(z_1)
plot(dens_1, col = "red", lwd = 2)
curve(dnorm(x, mean = 0, sd = 1), add = TRUE, col = "blue", lwd = 2)

dens_20 <- density(z_20)
plot(dens_20, col = "red", lwd = 2)
curve(dnorm(x, mean = 0, sd = 1), add = TRUE, col = "blue", lwd = 2)

dens_200 <- density(z_200)
plot(dens_200, col = "red", lwd = 2)
curve(dnorm(x, mean = 0, sd = 1), add = TRUE, col = "blue", lwd = 2)

# c)
n <- 30
p <- 0.5
x <- rbinom(1000, n, p)
hist(x, breaks = seq(-0.5, n+0.5, by = 1), freq = FALSE, xlab = "x", ylab = "density")
curve(dnorm(x, mean = n*p, sd = sqrt(n*p*(1-p))), add = TRUE, col = "red")

n <- 100
p <- 0.5
x <- rbinom(1000, n, p)
hist(x, breaks = seq(-0.5, n+0.5, by = 1), freq = FALSE, xlab = "x", ylab = "density")
curve(dnorm(x, mean = n*p, sd = sqrt(n*p*(1-p))), add = TRUE, col = "red")

n <- 30
p <- 0.1
x <- rbinom(1000, n, p)
hist(x, breaks = seq(-0.5, n+0.5, by = 1), freq = FALSE, xlab = "x", ylab = "density")
curve(dnorm(x, mean = n*p, sd = sqrt(n*p*(1-p))), add = TRUE, col = "red")

n <- 30
p <- 0.1
x <- rbinom(1000, n, p)
hist(x, breaks = seq(-0.5, n+0.5, by = 1), freq = FALSE, xlab = "x", ylab = "density")
curve(dnorm(x, mean = n*p, sd = sqrt(n*p*(1-p))), add = TRUE, col = "red")

n <- 100
p <- 0.1
x <- rbinom(1000, n, p)
hist(x, breaks = seq(-0.5, n+0.5, by = 1), freq = FALSE, xlab = "x", ylab = "density")
curve(dnorm(x, mean = n*p, sd = sqrt(n*p*(1-p))), add = TRUE, col = "red")