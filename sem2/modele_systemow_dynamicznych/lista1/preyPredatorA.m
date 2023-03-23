function preyPredatorA(xzero, yzero, params, T, dt, maxOrMinChoice, xyChoice)
    t = 0:dt:T;
    xprev = xzero;
    yprev = yzero;
    a = params(1);
    b = params(2);
    c = params(3);
    d = params(4);
    xvec = zeros(size(t));
    yvec = zeros(size(t));
    canBeReduced = true;
    reductionPercent = 0.9;
    
    for iter = 1:length(t)
        dxdt = (a - b * yprev) * xprev;
        dydt = (c * xprev - d) * yprev;

        xcurr = xprev + dxdt * dt;
        ycurr = yprev + dydt * dt;

        if canBeReduced && maxOrMinChoice == "max"% && t(iter) > 2
            if xyChoice == "x" && xcurr < xprev
                xcurr = xcurr * reductionPercent;
                canBeReduced = false;
            elseif xyChoice == "y" && ycurr < yprev
                ycurr = ycurr * reductionPercent;
                canBeReduced = false;
            end

        elseif canBeReduced && maxOrMinChoice == "min"% && t(iter) > 4
            if xyChoice == "x" && xcurr > xprev
                xcurr = xcurr * reductionPercent;
                canBeReduced = false;
            elseif xyChoice == "y" && ycurr > yprev
                ycurr = ycurr * reductionPercent;
                canBeReduced = false; 
            end
        end

        xvec(iter) = xcurr;
        yvec(iter) = ycurr;

        xprev = xcurr;
        yprev = ycurr;
    end

    plot(t, xvec, t, yvec, T, dt);
end