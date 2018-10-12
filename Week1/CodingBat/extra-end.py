def extra_end(str):
  if len(str)<3:
    return str+str+str
  else:
    return str[-2:]+str[-2:]+str[-2:]
