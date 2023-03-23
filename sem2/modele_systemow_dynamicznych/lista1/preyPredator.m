function preyPredator(xzero, yzero, params, T, dt)
    t = 0:dt:T;
    xprev = xzero;
    yprev = yzero;
    a = params(1);
    b = params(2);
    c = params(3);
    d = params(4);
    xvec = zeros(size(t));
    yvec = zeros(size(t));

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
    plot(t, xvec, "blue", t, yvec, "red", T, dt);
%    legend("Prey population", "Predator population");
end