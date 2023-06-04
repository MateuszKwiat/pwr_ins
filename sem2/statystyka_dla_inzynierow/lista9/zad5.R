# a)
data <- read.csv("waga1(1).csv", sep = ";")

data_m <- data[data$plec == 0,]
weight_bef_m <- data_m$Waga_przed
weight_aft_m <- data_m$Waga_po

mean_m <- mean(weight_aft_m - weight_bef_m)
sd_m <- sd(weight_aft_m - weight_bef_m)

z <- (mean_m - 4) / (sd_m / sqrt(length(weight_aft_m - weight_bef_m)))
z

p <- 2 * pnorm(z)
p

alpha <- 0.05

# mamy bardzo mocne dowody przeciwko sredniemu przyrostowi wagi m o 4
if(p < alpha) {
  cat("Studenci (mezczyzni) nie przytyli srednio o 4 kg.", alpha)
} else {
  cat("Studenci (mezczyzni) przytyli srednio o 4 kg.", alpha)
}
p

# mamy dowody przeciwko sredniemu przyrostowi wagi m o 4
z_critical <- qnorm(1 - alpha/2)
if(abs(z) > z_critical) {
  cat("Studenci (mezczyzni) nie przytyli srednio o 4 kg.", alpha)
} else {
  cat("Studenci (mezczyzni) przytyli srednio o 4 kg.", alpha)
}
z_critical


# b)
weight_diff <- weight_aft_m - weight_bef_m
mean_weight_diff <- mean(weight_diff)
sd_weight_diff <- sqrt(var(weight_diff))

t <- mean_weight_diff/(sd_weight_diff/sqrt(nrow(data_m)))
t_crit <- qt(1 - 0.05/2, df = length(nrow(data_m)-1))

# nie mamy dowodow przeciwko sredniemu przyrostowi wagi m o 4
if (abs(t) > abs(t_crit)) {
  cat("t =", t, "jest wieksze od ", t_crit)
} else {
  cat("t =", t, "jest mniejsze od ", t_crit)
}
t_crit


# c)      
diff <- weight_aft_m - weight_bef_m

t.test <- t.test(diff, mu=4)
t.test