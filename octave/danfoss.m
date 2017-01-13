function [data,date,time,x,y,z,Z]= danfoss(filename)
data=csvread(filename);
a=data;
a(:,1)=a(:,1)-42164;
a(1,1)=0;
a(1,:)=100*a(1,:);
y=a(1,:)(2:end);
x=a(:,1)(2:end);
u=a(2:end,2:end);
z=a;
Z=u;
date=a(:,1);
time=a(1,:);
endfunction