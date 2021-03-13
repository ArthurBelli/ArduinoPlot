my_file = './samples.csv'; #imports the csv
labels = fileread(my_file);
comma = index(labels, ",");
new_line = index(labels, "\n");
first_label = labels(1: comma-1);
second_label = labels(comma+1: new_line-1);
M = dlmread(my_file, ',', 1, 0); #parses the csv into a matrix
#M(1, :) gets all columns in the first row
plot(M(:, 1), M(:, 2),"b", M(:, 1), mean(M(:, 2)), "m")
xlabel(first_label);
ylabel(second_label);
title("Arduino Measures"); grid on
print -dpng ./graph.png -color
