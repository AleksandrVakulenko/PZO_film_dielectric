
load('Data_2022_12_20.mat')


Dia = 70e-6; %m
H = 50e-9; %m
Eps0 = 8.85e-12; %F/m

S = pi*(Dia/2)^2; %m^2

Eps = C*H/(S*Eps0);

figure('position', [552 248 729 733])

subplot(2,1,1)
plot(Temp, Eps)
xlim([20 360])
ylim([100 300])
ylabel('eps''')
xlabel('T, C')

subplot(2,1,2)
plot(Temp, D)
xlim([20 360])
ylim([0 0.15])
ylabel('D')
xlabel('T, C')













