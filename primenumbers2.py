z2_numbers_list = list(range(1,50000))

primenumbers = list()
flag = False

z2_numbers_list.sort()
last_element = z2_numbers_list[-1]

for i in z2_numbers_list:
  flag = False
  if i > 1: #this line is nonsense - discus indent problems ...
    for x in range (2,last_element):
      if (i > x):
        if ( i % x == 0):
          flag = True
          break
  if not flag and i > 1:
    primenumbers.append(i)

print (primenumbers[:-1])

print ("Finito... testing git update local files update")

#czy zawsze trzeba po zmianie w pliku zrobić add a potem commit?
