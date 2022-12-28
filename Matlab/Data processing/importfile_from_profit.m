function [temp, dEps1, f1, a1, dEps2, f2, a2, dEps3, f3, a3, SScm, EpsInf] ...
    = importfile_from_profit_2(filename)

dataLines = [2, Inf];


%% Setup the Import Options and import the data
opts = delimitedTextImportOptions("NumVariables", 25);

% Specify range and delimiter
opts.DataLines = dataLines;
opts.Delimiter = "\t";

% Specify column names and types
opts.VariableNames = ["temp", "Var2", "Var3", "Var4", "Var5", "Var6", "dEps1", "f1", "a1", "Var10", "dEps2", "f2", "a2", "Var14", "dEps3", "f3", "a3", "Var18", "Var19", "Var20", "Var21", "Var22", "SScm", "Var24", "EpsInf"];
opts.SelectedVariableNames = ["temp", "dEps1", "f1", "a1", "dEps2", "f2", "a2", "dEps3", "f3", "a3", "SScm", "EpsInf"];
opts.VariableTypes = ["double", "string", "string", "string", "string", "string", "double", "double", "double", "string", "double", "double", "double", "string", "double", "double", "double", "string", "string", "string", "string", "string", "double", "string", "double"];

% Specify file level properties
opts.ExtraColumnsRule = "ignore";
opts.EmptyLineRule = "read";

% Specify variable properties
opts = setvaropts(opts, ["Var2", "Var3", "Var4", "Var5", "Var6", "Var10", "Var14", "Var18", "Var19", "Var20", "Var21", "Var22", "Var24"], "WhitespaceRule", "preserve");
opts = setvaropts(opts, ["Var2", "Var3", "Var4", "Var5", "Var6", "Var10", "Var14", "Var18", "Var19", "Var20", "Var21", "Var22", "Var24"], "EmptyFieldRule", "auto");
opts = setvaropts(opts, ["temp", "dEps1", "f1", "a1", "dEps2", "f2", "a2", "dEps3", "f3", "a3", "SScm", "EpsInf"], "FillValue", 0);
opts = setvaropts(opts, ["temp", "dEps1", "f1", "a1", "dEps2", "f2", "a2", "dEps3", "f3", "a3", "SScm", "EpsInf"], "DecimalSeparator", ",");

% Import the data
tbl = readtable(filename, opts);

%% Convert to output type
temp = tbl.temp;
dEps1 = tbl.dEps1;
f1 = tbl.f1;
a1 = tbl.a1;
dEps2 = tbl.dEps2;
f2 = tbl.f2;
a2 = tbl.a2;
dEps3 = tbl.dEps3;
f3 = tbl.f3;
a3 = tbl.a3;
SScm = tbl.SScm;
EpsInf = tbl.EpsInf;
end