# a)
nums <- sample(c(0:3), 600, TRUE, c(0.3, 0.4, 0.2, 0.1))

# b)
mean(nums)
sd(nums)

# c)
as.data.frame(table(nums))
