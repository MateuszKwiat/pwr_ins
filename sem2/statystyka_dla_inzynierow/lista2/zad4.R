# a)
# w 5 min 5 * 3.5 = 17.5
dpois(16, 17.5)

# b)
1 - ppois(19, 17.5)

# c)
ppois(12, 17.5) - dpois(12, 17.5)

# d)
# 14 <= X < 22
# p(x <= k2) - p(x<= k1 -1 )
(ppois(22, 17.5) - dpois(22, 17.5)) - ppois(13, 17.5)
