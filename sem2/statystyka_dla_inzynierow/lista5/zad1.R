# a)
d <-  matrix(c(1/8, 1/6, 1/4, 1/6, 1/8, 1/6), nrow = 2, ncol = 3);
d;

print("P(Y=0)"); 
sum(d[,1])
print("P(Y=1)")
sum(d[,2])
print("P(Y=2)")
sum(d[,3])

print("P(X=0)")
sum(d[1,])
print("P(X=1)")
sum(d[2,])

# b)
cor(d)


# c)
py0x0 <- data[1,1] / sum(data[1,]);
py1x0 <- data[1,2] / sum(data[1,]);
py2x0 <- data[1,3] / sum(data[1,]);

py0x1 <- data[2,1] / sum(data[2,]);
py1x1 <- data[2,2] / sum(data[2,]);
py2x1 <- data[2,3] / sum(data[2,]);

print("P(Y=0|X=0)"); py0x0
print("P(Y=1|X=0)"); py1x0
print("P(Y=2|X=0)"); py2x0

print("P(Y=0|X=1)"); py0x1
print("P(Y=1|X=1)"); py1x1
print("P(Y=2|X=1)"); py2x1

