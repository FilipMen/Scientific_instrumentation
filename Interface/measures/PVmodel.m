Tc = 25+273.15; % Temperature in K
%G = 1000; % Solar insulation in W/m^2
V = 2; % Output voltage

for G=100:100:1000
    [II,VV]=I_fun(Tc,G,0.01);
    Isc(G/100)=II(1);
    plot(VV,II)
    hold on
    grid on
end

figure
plot(Isc,100:100:1000)