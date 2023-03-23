dt = 0.001;
T = 20;
t = 0:dt:T;
params = [1.2, 0.6, 0.3, 0.8];
%params = [1.2, 0.6, 0.3, 0.8];
xzero = -0.2;
yzero = 2;
preyPredator(xzero, yzero, params, T, dt);

maxOrMinChoice = "min"; % assign "max" or "min" string
xyChoice = "y"; % assign "x" or "y" string
%preyPredatorA(xzero, yzero, params, T, dt, maxOrMinChoice, xyChoice);