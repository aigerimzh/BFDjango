def missing_char(str, n):
  l = []
  l = list (str)
  l.pop(n) 
  return ("".join(l))
