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
    plot(X,Y)
    hold on
    Area(k) = trapz(X,Y);
    figure(3)
    plot(X,P)
    hold on


end
figure(2)
hold off
figure(3)
hold off
figure(4)
scatter(number, Area)
hold on 
pI = polyfit(number, Area, 1);
Irradiance = 400:100:900;
Measure = polyval(pI, Irradiance);
plot(Irradiance, Measure)

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

yfit = polyval(pI,unique(number));
y = areaU;
yresid = y - yfit;
SSresid = sum(yresid.^2);
SStotal = (length(y)-1) * var(y);
rsq_adj = 1 - SSresid/SStotal * (length(y)-1)/(length(y)-length(pI))

