var
  f: text;
  s, n, sum, r, max: longword;
  a: array of longword;

begin
  assign(f, '../data/26-15.txt');
  reset(f);
  read(f, s, n);
  SetLength(a, n);
  for i: longword := 0 to n - 1 do
    readln(f, a[i]);
  sort(a);
  while (sum <= s) do
  begin
    sum += a[r];
    inc(r);
  end;
  sum -= a[r - 1]; 
  for i: longword := r - 1 to n - 1 do
    if (sum - a[r - 2] + a[i] <= s) then
      max := a[i];
  write(r - 1, ' ', max)
end.
