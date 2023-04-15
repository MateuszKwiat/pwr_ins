# a)
kumulacja <- apply(data, 2, cumsum)
kumulacja

X <- rep(0:1, each = 500)
Y <- numeric(length = 1000)

for(i in 1:1000) {
  u <- runif(1)
  Y[i] <- sum(kumulacja[, X[i] + 1] <= u)
}

realizacja <- cbind(X, Y)
head(realizacja)

