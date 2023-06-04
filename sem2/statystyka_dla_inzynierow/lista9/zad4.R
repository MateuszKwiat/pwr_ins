# a)
data <- read.csv("waga1(1).csv", sep=";")

mean_bef <- mean(data$Waga_przed)
mean_aft <- mean(data$Waga_po)

mean_diff <- mean_aft - mean_bef

sd <- sqrt(var(data$Waga_po - data$Waga_przed))
z <- mean_diff/(sd/sqrt(nrow(data)))

p <- 2*(1 - pnorm(abs(z)))
alpha <- 0.05

# mamy bardzo mocne dowody przeciwko sredniemu przyrostowi wagi o 2
if(p < alpha) {
  cat("Nieprawda ze, wszyscy studenci przytyli srednio o 2 kg.", alpha)
} else {
  cat("Wszyscy studenci przytyli srednio o 2 kg.", alpha)
}
p

# mamy dowody przeciwko sredniemu przyrostowi wagi o 2
z_critical <- qnorm(1 - alpha/2)
if(abs(z) > z_critical) {
  cat("Nieprawda ze, wszyscy studenci przytyli srednio o 2 kg.", alpha)
} else {
  cat("Wszyscy studenci przytyli srednio o 2 kg.", alpha)
}
z_critical


# b)
weight_diff <- data$Waga_po - data$Waga_przed
mean_weigth_diff <- mean(weight_diff)
sd_weight_diff <- sqrt(var(weight_diff))

# nie mamy dowodu przeciwko
t <- mean_weigth_diff/(sd_weight_diff/sqrt(nrow(data)))
t_crit <- qt(1 - 0.05/2, df = length(nrow(data)-1))
if (abs(t) > abs(t_crit)) {
  cat("t =", t, "jest wieksze od ", t_crit)
} else {
  cat("t =", t, "jest mniejsze od ", t_crit)
}
t_crit

             

# c)
diff <- data$Waga_po - data$Waga_przed

t_test <- t.test(diff, mu=2)
t_test