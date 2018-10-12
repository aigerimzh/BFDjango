def last2(str):
  cnt = 0
  if len (str) < 2:
    return 0
  for x in range(len(str)-2):
    if str[x:x+2] == str[len(str)-2:]:
      cnt = cnt + 1
  return cnt
