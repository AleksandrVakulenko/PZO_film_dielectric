function [Temp, C, D, R, X] = importfile(filename)


dataLines = [2, Inf];


%% Set up the Import Options and import the data
opts = delimitedTextImportOptions("NumVariables", 6);

% Specify range and delimiter
opts.DataLines = dataLines;
opts.Delimiter = " ";

% Specify column names and types
opts.VariableNames = ["Temp", "Var2", "C", "D", "R", "X"];
opts.SelectedVariableNames = ["Temp", "C", "D", "R", "X"];
opts.VariableTypes = ["double", "string", "double", "double", "double", "double"];

% Specify file level properties
opts.ExtraColumnsRule = "ignore";
opts.EmptyLineRule = "read";
opts.ConsecutiveDelimitersRule = "join";
opts.LeadingDelimitersRule = "ignore";

% Specify variable properties
opts = setvaropts(opts, "Var2", "WhitespaceRule", "preserve");
opts = setvaropts(opts, "Var2", "EmptyFieldRule", "auto");

% Import the data
tbl = readtable(filename, opts);

%% Convert to output type
Temp = tbl.Temp;
C = tbl.C;
D = tbl.D;
R = tbl.R;
X = tbl.X;
end