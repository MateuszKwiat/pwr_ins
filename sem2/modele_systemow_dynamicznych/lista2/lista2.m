out = sim("lista2_lorenzslx.slx");
xData = get(out, "simout");
yData = get(out, "simout1");
zData = get(out, "simout2");

plot3(xData, yData, zData);
