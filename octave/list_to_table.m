function A = list_to_table (list_of_vects)
  x1 = list_of_vects(:,1);
  x2 = list_of_vects(:,2);
  z  = list_of_vects(:,3);
  dims=[max(x2), max(x1)];
  A=zeros(dims);
  for i=1:length(x1)
    A(x2(i), x1(i)) = z(i);
end
endfunction