i <- 0;
while (i < 50) {
  lam <- 3;
  x <- 0;
  p <- exp(-lam);
  s <- p;
  u <- runif(1, 0, 1);
  while (s < u) {
    x <- x + 1;
    p <- lam * p / x;
    s <- s + p;
  }
  print(x)
  i <- i + 1;
}