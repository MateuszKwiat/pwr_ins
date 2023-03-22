# a)
imie <- c("Krzysztof", "Maria", "Henryk", "Anna");
plec <- c("m", "k", "m", "k");
analiza <- c(3.5, 4.5, 5.0, 4.5);
algebra <- c(4.0, 5.0, 4.0, 3.5);
df1 <- data.frame(imie, plec, analiza, algebra);

# b)
print(df1[1,]);
print(df1[2,]);

# c)
str(df1)

# d)
av <- sum(df1[,3])/length(df1[,3]);

# e)
srednia <- c();
iter <- c(1:4);

for(i in iter) {
  srednia[i] <-(df1[i,3] + df1[i,4]) / 2;
}
df1 <- cbind(df1, srednia);

# f)
df2 <- data.frame();
for (i in iter) {
  if (df1[i,2] == "k") {
    df2 <- rbind(df2, df1[i,]);
  }
}

# g)
df3 <- data.frame();
for (i in iter) {
  if (df1[i,3] >= 4.5 | df1[i,4] >= 4.5) {
    df3 <-rbind(df3, df1[i,]);
  }
}

# h)
count <- 0;
for (i in iter) {
  if (df1[i,3] >= 4.5) {
    count <- count + 1;
  }
}

print(count)