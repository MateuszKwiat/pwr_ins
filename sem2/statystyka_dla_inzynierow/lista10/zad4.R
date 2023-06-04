# a)
dane <- read.csv("waga1(1).csv", sep=";")

weights_female <- dane$Waga_po[dane$plec == 1]
weights_male <- dane$Waga_po[dane$plec == 0]

mean_female <- mean(weights_female)
mean_male <- mean(weights_male)

var_female <- var(weights_female)
var_male <- var(weights_male)

n_female <- length(weights_female)
n_male <- length(weights_male)
se <- sqrt((var_female/n_female) + (var_male/n_male))
z <- (mean_female - mean_male) / se

p <- 2 * (1 - pnorm(abs(z)))
alpha <- 0.05

if (p < alpha) {
  cat("Odrzucenie hipotezy")
} else {
  cat("Brak podstaw do odrzucenia hipotezy")
}
p

z_critical <- qnorm(1 - alpha/2) 
if(abs(z) > z_critical) {
  cat("Odrzucenie hipotezy")
} else {
  cat("Brak podstaw do odrzucenia hipotezy")
}
z_critical

# b)
p <- t.test(weights_female, weights_male)

if (p$p.value < 0.05) {
  cat("Odrzucenie hipotezy")
} else {
  cat("Brak podstaw do odrzucenia hipotezy")
}
p
