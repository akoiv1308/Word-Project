word = input("Enter a word: ")
number = int(input("How many are there?"))

#Operations that determine the last letters of the words 
last1letter = word[-1:]
last2letters = word[-2:]
last3letters = word[-3:]
last4letters = word[-4:]

#If there is more than one "thing"...
if number > 1:
  if last2letters == "fe":
    print (("There are ") + str(number) + (" ") + (word [:-2])+ ("ves"))
  elif last2letters == "ch" or last2letters == "sh":
    print (("There are ") + str(number) + (" ") + (word)  + ("es"))
  #Special case 1
  elif last1letter == "s":
    print (("There are ") + str(number) + (" ") + (word) + ("es"))
  elif last2letters == "us":
    print (("There are ") + str(number) + (" ") + (word [:-2])+ ("i"))
  elif last2letters == "ay" or last2letters == "oy" or last2letters == "ey" or last2letters == "uy":
    print (("There are ") + str(number) + (" ") + (word) + ("s"))
  #Special case 2
  elif last4letters == "ooth":
    print (("There are ") + str(number) + (" ") + (word[:-4]) + ("eeth"))
  #Special case 3
  elif last4letters == "ouse":
    print (("There are ") + str(number) + (" ") + (word[:-4]) + ("ice"))
  #Special case 4
  elif last3letters == "eau":
    print (("There are ") + str(number) + (" ") + (word) + ("x"))
  elif last1letter == "y":
    print (("There are ") + str(number) + (" ") + (word[:-1]) + ("ies"))
  #Special case 5
  elif last2letters == "is":
    print (("There are ") + str(number) + (" ") + (word[:-2]) + ("es"))
  #Special case 6
  elif last1letter == "x":
    print (("There are ") + str(number) + (" ") + (word) + ("es"))
  else:
    print (("There are ") + str(number) + (" ") + (word) + ("s"))
elif number == 1:
  #If there is only one "thing"...
  print (("There is ") + str(number) + (" ") + (word))
elif number == 0:
  #If there is no "thing"...
  if last1letter == "s":
    print (("There are no ") + (word) + ("es"))
  elif last4letters == "ooth":
    print (("There are no ") + (word[:-4]) + ("eeth"))
  elif last4letters == "ouse":
    print (("There are no ") + (word[:-4]) + ("ice"))
  elif last3letters == "eau":
    print (("There are no ") + (word) + ("x"))
  elif last2letters == "ix":
    print (("There are no ") + (word[:-2]) + ("ices"))
  elif last1letter == "x":
    print (("There are no ") + (word) + ("es"))
  else:
    print (("There are no ") + (word) + ("s"))

print ("Thanks for testing the programm :) Have a nice day!")

  
'''
#Explanation : 
(("There are ") + (how much do we have?) + (" ") + (word(what word are we we trying to cut and how many letters do we need to remove?)) + (add a new last letters to the old word)
'''




