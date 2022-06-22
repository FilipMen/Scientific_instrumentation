function [II,VV] = I_fun(Tc,G,step)
q = 1.6e-19; % Electron charge
k = 1.38e-23; % Boltzmann's constant
Isc = 0.22; % Short circuit current
Voc = 2; % Open circuit voltage
n = 1.1; % Ideality factor
Tref = 25+273.15; % Reference temperature in K
Gref = 1000; % Solar insolation reference in W/m^2
Eg = 1.10; % Bang-gap energy of the Si solar cell [eV]
KI = 1.7e-3; % Solar short-circuit current temperature coefficient
Rs = 1e-2; % Series resistance
Rsh = 300; % Shunt resistance
cont = 1;
V = 0;
I = inf;
while(I>0)
    syms I
    Vt = k*Tc/q;
    Irs = Isc/(exp(q*Voc/(n*k*Tc))-1);
    Is = Irs*(Tc/Tref)^3*exp(q*Eg/(n*k)*(1/Tref-1/Tc));
    Iph = (Isc+KI*(Tc-Tref))*G/Gref;
    Id = Is*(exp((V+I*Rs)/(n*Vt))-1);
    Ish = (V+I*Rs)/Rsh;
    fun = matlabFunction(Iph-Id-Ish-I);
    I = fsolve(fun,0);
    II(cont) = I;
    VV(cont) = V;
    if I<0
        VV(cont) = interp1(II,VV,0);
        II(cont) = 0;
    end
    cont = cont+1;
    V = V+step;
end