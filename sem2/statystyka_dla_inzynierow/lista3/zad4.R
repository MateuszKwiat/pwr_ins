# a)
1 - pnorm(180, 170, 12);

# b)
pnorm(165, 170, 12);

# c)
pnorm(190, 170, 12) - pnorm(155, 170, 12);

# d)
x <- seq(130, 210, 1);
plot(x, dnorm(x, 170, 12), type = "l");