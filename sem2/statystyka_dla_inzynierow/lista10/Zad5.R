# a)
dane <- read.csv("waga1(1).csv", sep=";")

weights_above_70_female <- sum(dane$Waga_po[dane$plec == 1] > 70)
weights_above_70_male <- sum(dane$Waga_po[dane$plec == 0] > 70)

prop_above_70_female <- weights_above_70_female / length(dane$plec[dane$plec == 1])
prop_above_70_male <- weights_above_70_male / length(dane$plec[dane$plec == 0])

se_female <- sqrt((prop_above_70_female * (1 - prop_above_70_female)) / length(dane$plec[dane$plec == 1]))
se_male <- sqrt((prop_above_70_male * (1 - prop_above_70_male)) / length(dane$plec[dane$plec == 0]))

z <- (prop_above_70_female - prop_above_70_male) / sqrt(se_female^2 + se_male^2)
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
weights_female <- dane$Waga_po[dane$plec == 1]
weights_male <- dane$Waga_po[dane$plec == 0]



p <- prop.test(weights_female > 70, weights_male > 70)

if (p$p.value < 0.05) {
  cat("Odrzucenie hipotezy")
} else {
  cat("Brak podstaw do odrzucenia hipotezy")
}
p
