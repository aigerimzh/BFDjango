def not_string(str):
  if str.find("not") == -1 or str.find("not") != 0 :
    return "not "+str
  else:
    return str
    
