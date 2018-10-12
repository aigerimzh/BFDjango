def string_splosion(str):
  l = []
  l = list(str)
  ll = []
  for x  in range(len(l)):
    ll.append(str[0:x])
  ll.append(str)
  return "".join(ll)
