clear all
close all
clc

MyFolderInfo = dir;
cont = 1;
for i = 1:length(MyFolderInfo)
    file = MyFolderInfo(i).name;
    fileName = split(file,'.');
    if fileName(end) == "csv"
        aux = split(fileName(1),'_');
        aux = strrep(aux(end),'(','_');
        aux = strrep(aux(end),')','_');
        ans = split(aux,'_');
        number(cont) = str2num(ans{1});
        data.("i"+aux) = importdata(file);
        cont = cont +1;
    end
end

fn = fieldnames(data);
for k=1:numel(fn)
    X = data.(fn{k})(:,1);
    Y = data.(fn{k})(:,2)/23.6;

    X = sort(X);
    Y = sort(Y,'descend');
    P = X.*Y;
    figure(2)
    plot(X,Y*1000, 'LineWidth', 1)
    hold on
    grid on
    xlabel('Voltage [V]')
    ylabel('Current [mA]')
    title('Measurements VI curves')
    Area(k) = trapz(X,Y);
    figure(3)
    plot(X,P, 'LineWidth', 1)
    grid on
    hold on
    xlabel('Voltage [V]')
    ylabel('Power [W]')
    title('Measurements power curves')


end
figure(2)
hold off
figure(3)
hold off
figure(4)
scatter(Area, number, 300, 'k','.')
hold on
grid on
ylabel('Solar irradiance [W/m^2]')
xlabel('Total power [W]')
title('Calibration curve')
pI = polyfit(Area, number, 1);
Measure = 0.08:0.01:0.28;
Irradiance = polyval(pI, Measure);
plot(Measure, Irradiance, 'LineWidth', 1)

irrU = unique(number);
for i = 1:length(irrU)
    prom = 0;
    cont = 0;
    for j = 1:length(number)
        if irrU(i) == number(j)
            cont = cont+1;
            prom = prom+Area(j);
        end
        areaU(i) = prom/cont;
    end
end

yfit = polyval(pI,areaU);
y = irrU;
yresid = y - yfit;
SSresid = sum(yresid.^2);
SStotal = (length(y)-1) * var(y);
rsq_adj = 1 - SSresid/SStotal * (length(y)-1)/(length(y)-length(pI))

