# a)
mean_IQ <- 109
sd_IQ <- sqrt(225)

n <- 100

z = (mean_IQ - 105) / (sd_IQ / sqrt(n))

p <- 2 * (1 - pnorm(abs(Z)))
alpha <- 0.05

# mamy mocne dowody przeciwko sredniej 105 
if(p < alpha) {
  cat("Sredni wskaznik inteligencji nie wynosi 105", alpha)
} else {
  cat("Sredni wskaznik inteligencji wynosi 105", alpha)
}
p


z_critical <- qnorm(1 - alpha/2)
# mamy dowody przeciwko sredniej 105
if(abs(z) > z_critical) {
  cat("Sredni wskaznik inteligencji nie wynosi 105", alpha)
} else {
  cat("Sredni wskaźnik inteligencji wynosi 105", alpha)
}
z_critical


# b)
mean_IQ <- 109
sd_IQ <- sqrt(225)

n <- 100
t <- (mean_IQ - 105) / (sd_IQ / sqrt(n))

t_crit <- qt(1 - 0.05/2, df = n-1)

# mamy dowody przeciwko sredniej 105
if (abs(t) > abs(t_crit)) {
  cat("t =", t, "jest wieksze od ", t_crit)
} else {
  cat("t =", t, "jest mniejsze od ", t_crit)
}
t_crit
t
