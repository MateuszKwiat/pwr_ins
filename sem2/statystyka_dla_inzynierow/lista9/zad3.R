# a)
data <- read.csv("waga1(1).csv", sep=";")

male_data <- subset(data, plec == 0)

mean_male <- mean(male_data$Wzrost)
sd_male <- sd(male_data$Wzrost)

z <- (mean_male - 172) / (sd_male / sqrt(length(male_data$Wzrost)))
p <- 2 * (1 - pnorm(abs(z)))

alpha <- 0.05

# nie ma dowodow przeciwko sredniemu wzrostowi m = 172
if(p < alpha) {
  cat("Sredni wzrost studentow (mezczyzn) nie wynosi 172cm", alpha)
} else {
  cat("Sredni wzrost studentow (mezczyzn) wynosi 172cm.", alpha)
}
p

# nie ma dowodow przeciwko sredniemu wzrostowi m = 172
z_critical <- qnorm(1 - alpha/2)
if(abs(z) > z_critical) {
  cat("Sredni wzrost studentow (mezczyzn) nie wynosi 172cm", alpha)
} else {
  cat("Sredni wzrost studentow (mezczyzn) wynosi 172cm.", alpha)
}
z_critical


# b)
t <- (mean_male - 172) / (sd_male / sqrt(length(male_data$Wzrost)))
t_crit <- qt(1 - 0.05/2, df = length(male_data$Wzrost)-1)

# nie ma dowodow przeciwko sredniemu wzrostowi m = 172
if (abs(t) > abs(t_crit)) {
  cat("t =", t, "jest wieksze od ", t_crit)
} else {
  cat("t =", t, "jest mniejsze od ", t_crit)
}
t_crit


# c)
t_test <- t.test(male_data$Wzrost, mu = 172)
t_test
