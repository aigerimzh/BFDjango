def front_times(str, n):
  s = ""
  if len(str) < 3:
    for x in range(n):
      s = s + str
    return s
  else:
    for x in range(n):
      s = s + str[0:3]
    return s
