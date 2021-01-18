var
  f: text;
  i, g: longword;
  c: char;

begin
  assign(f, '../data/24-5.txt');
  reset(f);
  while i < 10000 do
  begin
    read(f, c);
    if c = '(' then i += 1;
    g += 1;
  end;
  write(g);
  close(f);
end.
