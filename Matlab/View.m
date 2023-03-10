
% load('Data_2022_12_20.mat')
% Temp_lim = [20 360];
% Dia = 70e-6; %m
% H = 50e-9; %m

% load('Data_2022_12_21.mat')
% Temp_lim = [20 450];
% Dia = 70e-6; %m
% H = 100e-9; %m

% load('Data_2022_12_22.mat')
% Temp_lim = [20 450];
% Dia = 70e-6; %m
% H = 100e-9; %m

load('Data_2022_12_22_2.mat')
Temp_lim = [20 450];
Dia = 70e-6; %m
H = 100e-9; %m

Eps0 = 8.85e-12; %F/m

S = pi*(Dia/2)^2; %m^2

Eps = C*H/(S*Eps0);

Eps2 = Eps.*D;

Temp = Temp*(0.73 + 0.1); % TEMP COMPENSATION

Temp_heat = Temp(1:round(end/2));
Temp_cool = Temp(round(end/2)+1:end);
Eps1_heat = Eps(1:round(end/2));
Eps1_cool = Eps(round(end/2)+1:end);
Eps2_heat = Eps2(1:round(end/2));
Eps2_cool = Eps2(round(end/2)+1:end);
D_heat = D(1:round(end/2));
D_cool = D(round(end/2)+1:end);

figure('position', [552 248 729 733])

subplot(2,1,1)
hold on
plot(Temp_heat, Eps1_heat, 'r')
plot(Temp_cool, Eps1_cool, 'b')
xlim(Temp_lim)
% ylim([100 300])
ylabel('Eps''')
xlabel('T, C')

subplot(2,1,2)
hold on
plot(Temp_heat, Eps2_heat, 'r')
plot(Temp_cool, Eps2_cool, 'b')
xlim(Temp_lim)
% ylim([0 0.6])
ylabel('Eps"')
xlabel('T, C')

% subplot(2,1,2)
% hold on
% plot(Temp_heat, D_heat, 'r')
% plot(Temp_cool, D_cool, 'b')
% xlim(Temp_lim)
% % ylim([0 0.6])
% ylabel('D')
% xlabel('T, C')










