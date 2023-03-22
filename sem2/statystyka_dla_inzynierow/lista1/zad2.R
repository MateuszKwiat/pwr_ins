# a)
df1 <- data.frame(read.table("waga1.csv", header = TRUE, sep = ";"));

# b)
for (i in c(1:5)) {
  print(df1[i,]);
}

# c)
str(df1)

# d)
avgh <- sum(df1[,2])/length(df1[,2]);
avgwb <- sum(df1[,3])/length(df1[,3]);

# e)
iter <- c(1:length(df1[,1]));
W <- c();
for (i in iter) {
  W[i] <- df1[i,3]/((df1[i,2] * 0.01)^2);
}
df1 <- cbind(df1, W);

# f)
df2 <- data.frame();
for (i in iter) {
  if (df1[i,1] == 1 & df1[i,5] > 25) {
    df2 <- rbind(df2, df1[i,]);
  }
}

# g)
df3 <- data.frame();
for (i in iter) {
  if (df1[i,1] == 0) {
    df3 <- rbind(df3, df1[i,]);
  }
}

# h)
count <-0;
for (i in iter) {
  if (df1[i,2] > 175) {
    count <- count + 1;
  }
}
print(count)