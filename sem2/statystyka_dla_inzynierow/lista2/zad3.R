# a)
dbinom(27, 180, 1/6)

# b)
1 - pbinom(31, 180, 1/6)

# c)
pbinom(29, 180, 1/6) - dbinom(29, 180, 1/6)

# d)
# 25 <= x <= 33
# p(x <= k2) - p(x<= k1 -1 )
pbinom(33, 180, 1/6) - pbinom(24, 180, 1/6)
