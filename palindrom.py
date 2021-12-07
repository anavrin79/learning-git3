def palindrom(string):
  counter = 1
  #reversedstring=list()
  for i in string:
    #print (string[2])
    if string[counter-1]==string[-counter]:
      palindrom = True
    else:
      palindrom = False
      break
  if (palindrom):
    print(string + " jest palindromem.")
  else:
    print(string + " nie jest palindromem.")


palindrom("akta generała ma mała renegatka")