# a)
data <- read.csv("waga1(1).csv", sep=";")

mean_height <- mean(data$Wzrost)
sd_height <- sd(data$Wzrost)

n <- length(data$Wzrost)
z <- (mean_height - 168) / (sd_height / sqrt(n))
p <- 2 * (1 - pnorm(abs(z)))
alpha <- 0.05

# mamy dowody przeciwko sredniemu wzrostowi = 168
if(p < alpha) {
  cat("Sredni wzrost studentow nie wynosi 168cm.", alpha)
} else {
  cat("Sredni wzrost studentow wynosi 168cm.", alpha)
}
p

# mamy dowody przeciwko sredniemu wzrostowi = 168
z_critical <- qnorm(1 - alpha/2)
if(abs(z) > z_critical) {
  cat("Sredni wzrost studentow nie wynosi 168cm.", alpha)
} else {
  cat("Sredni wzrost studentow wynosi 168cm.", alpha)
}
z_critical


# b)
mean_height <- mean(data$Wzrost)
sd_height <- sd(data$Wzrost)
t <- (mean_height - 168) / (sd_height / sqrt(length(data$Wzrost)))
t_crit <- qt(1 - 0.05/2, df = length(data$Wzrost)-1)

# mamy dowody przeciwko sredniemu wzrostowi = 168
if (abs(t) > abs(t_crit)) {
  cat("t =", t, "jest wieksze od ", t_crit)
} else {
  cat("t =", t, "jest mniejsze od ", t_crit)
}
t_crit


# c)
t_test <- t.test(data$Wzrost, mu = 168)
t_test
