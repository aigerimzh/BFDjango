def string_match(a, b):
  cnt = 0
  minl = min(len(a),len(b))
  for x in range(minl-1):
    if a[x:x+2] == b[x:x+2]:
      cnt = cnt + 1
  return cnt
