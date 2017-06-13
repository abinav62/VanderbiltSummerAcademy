# Name:
# Date:

"""
proj04

Asks the user for a string and prints out whether or not the string is a palindrome.

"""

string = raw_input("Type in a word: ")
derp = list(string)
stringList = []
for x in derp:
    if x != ' ':
        stringList.append(x)
    else:
        pass
li = []

for letter in stringList[-1:0:-1]:
    if letter != ' ':
        li.append(letter)
    else:
        pass

li.append(stringList[0])
str1 = ''.join(li)
str2 = ''.join(stringList)

if str1.lower() == str2.lower():
    print "This word or phrase is a palindrome."
else:
    print "This word or phrase is not a palindrome"