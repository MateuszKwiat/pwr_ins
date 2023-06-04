dane <- read.csv("waga1(1).csv", sep=";")

heights_female <- dane$Wzrost[dane$plec == 1]
heights_male <- dane$Wzrost[dane$plec == 0]

t <- t.test(heights_male, heights_female, mu = 5)
t

