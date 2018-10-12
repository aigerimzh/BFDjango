def cat_dog(str):
    cnt_d = 0
    cnt_c = 0
    for x in range (len(str)-2):
        if str[x] == 'c':
            if str[x+1]== 'a' and str[x+2]== 't':
                cnt_c = cnt_c +1
        elif str[x]== 'd':
            if str[x+1] == 'o' and str[x+2]== 'g':
                cnt_d = cnt_d +1
    if cnt_d == cnt_c:
      return True
    else:
      return False
