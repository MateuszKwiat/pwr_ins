# a)
dane <- read.csv("waga1(1).csv", sep=";")

n_female <- sum(dane$plec == 1)
p0 <- n_female / nrow(dane)
Z <- (p0 - 0.5) / sqrt(0.5 * (1 - 0.5) / nrow(dane))
alpha <- 0.05
z_critical <- qnorm(1 - alpha/2)

if (p0 < alpha) {
  cat("Odrzucenie hipotezy")
} else {
  cat("Brak podstaw do odrzucenia hipotezy")
}
p0

z_critical <- qnorm(1 - alpha/2)

if(abs(z) > z_critical) {
  cat("Odrzucenie hipotezy")
} else {
  cat("Brak podstaw do odrzucenia hipotezy")
}  
z_critical

# b)
n_female <- sum(dane$plec == 1)
n_male <- sum(dane$plec == 0)

p <- prop.test(n_female, nrow(dane), p = 0.5)
if (p$p.value < 0.05) {
  cat("Odrzucenie hipotezy")
} else {
  cat("Brak podstaw do odrzucenia hipotezy")
}
p

