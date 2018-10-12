def cigar_party(cigars, is_weekend):
  if cigars>=40 and cigars<=60:
    return True
  else:
    if is_weekend ==True and cigars>60:
      return True
    else:
      return False
