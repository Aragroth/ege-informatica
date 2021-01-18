var
  f: text;
  k, n, r, t: longword;
  a: array of longword;

begin
  assign(f, '../data/B.txt');
  reset(f);
  read(f, n);
  SetLength(a, n);
  for i: longword := 0 to n - 1 do
  begin
    readln(f, a[i]);
    if a[i] mod 13 = 0 then inc(k);
  end;
  for i: longword := 0 to n - 1 do
    if a[i] mod 13 = 0 then
    begin
      for j: longword := 0 to n - 1 do
        if ((a[i] + a[j]) mod 2 = 1) and (a[j] <> 0) and (i <> j) then inc(t);
      inc(r); a[i] := 0;
      if r >= k then break;
    end;
  write(t)
end.
