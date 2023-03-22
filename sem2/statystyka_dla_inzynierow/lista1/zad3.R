# a)
df1 <- data.frame(read.table("mieszkania.csv", header = TRUE, sep = ";"));

# b)
for (i in c(1:6)) {
  print(df1[i,]);
}

# c)
str(df1)

# d)
avgm <- sum(df1[,2])/length(df1[,2]);
avgp <- sum(df1[,5])/length(df1[,2]);

# e)
mp <- c(1:length(df1[,1]));
for (i in c(1:length(df1[,1]))) {
  mp[i] <- df1[i,5]/df1[i,2];
}
df1 <- cbind(df1, mp);

# f)
df2 <- data.frame();
for (i in c(1:length(df1[,1]))) {
  if (df1[i,1] == "Psie Pole" & df1[i,5] < 400000) {
    df2 <- rbind(df2, df1[i,]);
  }
}

# g)
df3 <- data.frame();
for (i in c(1:length(df1[,1]))) {
  if (df1[i,1] == "Srodmiescie" & df1[i,2] > 60) {
    df3 <- rbind(df3, df1[i,]);
  }
}

# h)
count <- 0;
for (i in c(1:length(df1[,1]))) {
  if (df1[i,2] > 60 & df1[i,5] < 350000) {
    count <- count + 1;
  }
}
print(count)