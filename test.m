% Nov 16
% Converting CSV files to Matlab variable files in Batch


clc;
close all;
clear all;

matfiles = dir('*.csv');
for ind = 1:length(matfiles)
    disp 'Processing:';
    a = mat2str(matfiles(ind).name);
    disp a;
    a = strrep(a,'.csv','');
    importdata(matfiles(ind).name);
    ans = ans.data;
%     eval(sprintf('%s = M;',a));
    eval(sprintf('save %s;',a));
    clear a M 
end
disp 'Done ...';