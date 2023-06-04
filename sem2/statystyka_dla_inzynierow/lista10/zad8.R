dane <- read.csv("waga1(1).csv", sep=";")

n_male_above_170 <- sum(dane$plec == 0 & dane$Wzrost > 170)
n_female_above_170 <- sum(dane$plec == 1 & dane$Wzrost > 170)

p <- prop.test(c(n_male_above_170, n_female_above_170), c(sum(dane$plec == 0), sum(dane$plec == 1)))
p