# a)
n <- 1000
x <- 385
p0 <- 0.4

# Obliczanie statystyki testowej
p <- x / n
q <- 1 - p
z <- (p - p0) / sqrt(p0 * q / n)

# Obliczanie wartości p
P <- 2 * (1 - pnorm(abs(z)))

alpha <- 0.05

if (P < alpha) {
  cat("Odrzucenie hipotezy")
} else {
  cat("Brak podstaw do odrzucenia hipotezy")
}
P

#Porównanie wartości testu Z z odpowiednimi wartościami krytycznymi
z_critical <- qnorm(1 - alpha/2)

if(abs(z) > z_critical) {
  cat("Odrzucenie hipotezy")
} else {
  cat("Brak podstaw do odrzucenia hipotezy")
}
z_critical


# b)
n_female <- 520
x_female <- 220
n_male <- 480
x_male <- 165

# Obliczanie proporcji
p_female <- x_female / n_female
p_male <- x_male / n_male

# Obliczanie statystyki testowej
p <- p_female - p_male
var <- (p_female * (1 - p_female) / n_female) + (p_male * (1 - p_male) / n_male)

# Błąd standardowy różnicy proporcji
se <- sqrt(var)

# Statystyka testowa
z <- p / se 

P <- 2 * (1 - pnorm(abs(z)))

alpha <- 0.05

if (P < alpha) {
  cat("Odrzucenie hipotezy")
} else {
  cat("Brak podstaw do odrzucenia hipotezy")
}
p

#Porównanie wartości testu Z z odpowiednimi wartościami krytycznymi
z_critical <- qnorm(1 - alpha/2)

if(abs(z) > z_critical) {
  cat("Odrzucenie hipotezy")
} else {
  cat("Brak podstaw do odrzucenia hipotezy")
}
z_critical

#c

# Dane 
n_female <- 520
mean_female <- 166
var_female <- 100
n_male <- 480
mean_male <- 174
var_male <- 121

# Obliczanie statystyki testowej
se <- sqrt((var_female / n_female) + (var_male / n_male))
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
