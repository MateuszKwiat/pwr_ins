dt = 0.001;
T = 20;
t = 0:dt:T;
xvec = zeros(size(t));
yvec = zeros(size(t));
xprev = 2;
yprev = 1;
a = 1.2;
b = 0.6;
c = 0.3;
d = 0.8;

for iter = 1:length(t)
    dxdt = (a - b * yprev) * xprev;
    dydt = (c * xprev - d) * yprev;

    xcurr = xprev + dxdt * dt;
    ycurr = yprev + dydt * dt;

    xvec(iter) = xcurr;
    yvec(iter) = ycurr;

    xprev = xcurr;
    yprev = ycurr;
end

plot(t, xvec, t, yvec);
