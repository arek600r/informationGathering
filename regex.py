'''
Identifiers
\d any number
\D anything but a number
\s space
\S anthing but space
\w any character
\W anything but a character
. any character, except for a newlines
\b the whitespace around words
\. a period

Modifiers:

{1,3} we're expecting 1-3
+ Match 1 ore more
? Match 0 or more
* March 0 or more
$match the end of a string
^ matching a beginning of a string
| either or \d{1-3| | \w{5-6}
[] range or "variance" [1-5a-q-A-Z]
{x} ex[ectiong "x" amount

White Space Charactes:
\n new line
\s space
\t tab
\e escape
\f form feed
\r return

Dont Forget!:

. + * ? [ ] $ ^ ( ) { } | \

'''


import re
exampleString = """


Jessica is 15 years old, and Daniel is 27 years old
Edward is 97, and his grandfather, Oscar is 102"""

ages = re.findall(r'\d{1,3}', exampleString)
names = re.findall(r'[A -Z][a-z]*', exampleString)

print(ages)
print(names)

ageDict = {}

x = 0

for eachName in names:
    ageDict[eachName] = ages[x]
    x+=1
print(ageDict)