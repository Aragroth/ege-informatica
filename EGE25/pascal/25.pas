var
  max, max2, del, pr, max3: longword;

begin
  for i: longword := 286564 to 287270 do
  begin
    del := 0;
    for g: longword := 2 to i div 2 do
      if i mod g = 0 then begin pr := g; del += 1; end;
    del += 2;
    if del > max then begin max := del; max2 := i; max3 := pr; end else
    if del = max then
      if max2 < i then begin max2 := i; max3 := pr end
  end;
  write(max, ' ', max3)
end.