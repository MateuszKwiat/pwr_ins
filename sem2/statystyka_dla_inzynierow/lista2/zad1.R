# a)
dbinom(5, 6, .5)

# b)
#pbinom(6, 6, .5) - pbinom(2, 6, .5) 
1 - pbinom(2, 6, .5)

# c)
pbinom(4, 6, .5) - pbinom(3, 6, .5)

# d)
 plot(dbinom(0:6, 6, .5), type = "h")
