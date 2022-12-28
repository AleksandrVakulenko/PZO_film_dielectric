ColeCole=@(DEps, f, a, freq) DEps./(1+(1i*6.2832.*freq./f).^a);

clc

filename = '001_50_coeff.txt';

[temp, dEps1, f1, a1, dEps2, f2, a2, dEps3, f3, a3, SScm, EpsInf] ...
    = importfile_from_profit(filename);


%% calc all stuff
freq = 10.^linspace(log10(20), log10(300e3), 100);

Eps1_const = EpsInf + dEps2;
Eps1_const = repmat(Eps1_const, 1, numel(freq));

CC1 = ColeCole(dEps1, f1, a1, freq);
CC2 = ColeCole(dEps3, f3, a3, freq);

Eps_cplx = Eps1_const + CC1 + CC2;

%% plot eps' and eps" vs freq

for i = 1:size(Eps_cplx, 1)
    T = temp(i);
    
    eps1 = real(Eps_cplx(i,:));
    eps2 = -imag(Eps_cplx(i,:));
    
    subplot(2,1,1)
    hold on
    plot(freq, eps1)
    set(gca, 'xscale', 'log')
    
    subplot(2,1,2)
    hold on
    plot(freq, eps2)
    set(gca, 'xscale', 'log')
    
end


%% plot eps' and eps" vs Temp
clc
figure
for j = 30:10:size(Eps_cplx, 2)
    F = freq(j);
    disp(F)
    
    eps1 = real(Eps_cplx(:,j));
    eps2 = -imag(Eps_cplx(:,j));
    
    subplot(2,1,1)
    hold on
    plot(temp, eps1)
%     plot(temp, eps1-eps1(1))
%     set(gca, 'xscale', 'log')
    
    subplot(2,1,2)
    hold on
    plot(temp, eps2)
%     set(gca, 'xscale', 'log')
    
   
end



%% Fit S vs Temp

plot(temp, SScm, 'x')

temp_new = (temp - 50)/200;
SScm_new = SScm./max(SScm);













