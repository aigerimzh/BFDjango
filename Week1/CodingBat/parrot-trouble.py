def parrot_trouble(talking, hour):
  if talking == True and (hour == 7 or hour == 20):
    return False
  elif talking == True and (hour > 7 or hour < 20):
    return True
  else:
    return False
