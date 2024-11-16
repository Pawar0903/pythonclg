% Define x values
x = -10:0.1:10;  % From -10 to 10 with a step of 0.1

% Define a function y = x^2
y = x.^2;        % Element-wise squaring

% Plot the function
figure;         % Create a new figure window
plot(x, y);
title('Plot of y = x^2');
xlabel('x values');
ylabel('y values');
grid on;% Add grid lines to the plot