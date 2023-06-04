# a)
n <- 1000
x <- 385

# Test proporcji
p <- prop.test(x, n, p = 0.4)

if (p$p.value < 0.05) {
  cat("Odrzucenie hipotezy")
} else {
  cat("Brak podstaw do odrzucenia hipotezy")
}
p

#b

# Dane
n_female <- 520
x_female <- 220
n_male <- 480
x_male <- 165

# Test proporcji
p <- prop.test(c(x_female, x_male), c(n_female, n_male))

if (p$p.value < 0.05) {
  cat("Odrzucenie hipotezy")
} else {
  cat("Brak podstaw do odrzucenia hipotezy")
}
p
