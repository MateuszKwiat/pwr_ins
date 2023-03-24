# a)
# 4 na min
# T = 30s
pexp(0.5, 0.25);

# b)
1 - pexp(1/3, 0.25);

# c)
(pexp(4/3)) - (pexp(2/3));

# d)
1 - qexp(0.2, 0.25);

# e)
x <- seq(0, 3, 0.1);
plot(x, dexp(x, 0.25), type = "l")