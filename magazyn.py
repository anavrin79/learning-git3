import tabulate

def get_items(itemslist):
  header = itemslist[0].keys()
  rows = [x.values() for x in itemslist]
  print (tabulate.tabulate(rows, header))

items = [
  {"name":"Milk","quantity":"120","unit":"l","unit_price":"2.3"},
  {"name":"Sugar","quantity":"1000","unit":"kg","unit_price":"3"},
  {"name":"Flour","quantity":"12000","unit":"kg","unit_price":"1.2"},
  {"name":"Coffee","quantity":"15","unit":"kg","unit_price":"40"}
]

end = False

while (end!=True):
  option = input ("What would you like to do?: ")

  if (option == "exit"):
    exit()
  if (option == "show"):
    get_items(items)
  else:
    pass
