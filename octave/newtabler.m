function [x1,x2,indvar1,indvar2,depvar,heightmap]= newtabler(data)
a=data;
a(1,1)=0;
y=a(1,:)(2:end);
x=a(:,1)(2:end);
u=a(2:end,2:end);
z=a;
Z=u;
date=a(:,1);
time=a(1,:);
endfunction