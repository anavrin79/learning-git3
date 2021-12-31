def palindrom(string):
  counter = 0
  for i in string:
    if string[counter]==string[-(counter+1)]:
      palindrom = True
      counter += 1
    else:
      palindrom = False
      break
  if (palindrom):
    print(string + " jest palindromem.")
  else:
    print(string + " nie jest palindromem.")

palindrom("aktagenerałamamałarenegatka")
