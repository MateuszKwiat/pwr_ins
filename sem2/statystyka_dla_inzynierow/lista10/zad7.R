dane <- read.csv("waga1(1).csv", sep=";")

students_gaining_weight <- sum(dane$Waga_po > dane$Waga_przed)

p <- prop.test(students_gaining_weight, nrow(dane), p = 0.8)
p
