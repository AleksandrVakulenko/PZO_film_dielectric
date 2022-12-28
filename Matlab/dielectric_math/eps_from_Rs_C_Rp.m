clc

freq = 10.^(linspace(log10(20), log10(300000), 30));

surf = pi*(70e-6/2)^2; %m^2
h = 100e-9; %m
eps0 = 8.85e-12; %F/m
cap0 = eps0*surf/h;

R_series = 5000; %Ohm
R_parallel = 100e6; %Ohm
C = 1e-9; %F
X = 1./(2*pi*1i*freq*C);


% z_film = R_series + X; %series
% z_film = R.*X./(R + X); %parallel


z_film = X;

z_full = R_parallel.*z_film./(R_parallel + z_film);
z_full = R_series + z_full;


z1 = real(z_full);
z2 = imag(z_full);


eps_cpx = 1./(2*pi*cap0*freq.*(z1 + 1i*z2));
eps1 = imag(eps_cpx);
eps2 = real(eps_cpx);

% eps1 = -z2./(2*pi*cap0*freq.*(z1.^2+z2.^2));
% eps2 =  z1./(2*pi*cap0*freq.*(z1.^2+z2.^2));




figure('position', [220 326 1116 650])

subplot(2,2,1)
plot(freq, z1)
ylabel('z''')
set(gca, 'xscale', 'log')

subplot(2,2,3)
plot(freq, z2)
ylabel('z"')
set(gca, 'xscale', 'log')


subplot(2,2,2)
plot(freq, eps1)
ylabel('eps''')
% ylim([0 3000])
set(gca, 'xscale', 'log')

subplot(2,2,4)
plot(freq, eps2)
ylabel('eps"')
% xlim("manual")
% ylim([0 1500])
set(gca, 'xscale', 'log')








