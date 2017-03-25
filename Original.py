print("Sa-k passe Boss?!")
r = input("Guess the number:")
guess = int(r)
if guess == 5:
  print("You got it!")
else:
  while guess != 5: 
    print("That was wrong!")
    r = input("Guess the number:") 
print("The game is terminated!")
#This code was interesting: it looped as desired, but it was unable to provide feedback to wrong answers like too high or too low.
#I want to be able to write a program that tells the user "Getting closer", "Too high", "Too Low"


#How do I activate syntax highlighting here?
#Answer: type in .py at the end of the file's name.
'''
#This code is a working code from Khan Academy
a = input("Guess my age: ")
while a > "26":
    print("Nope! Too high!")
    a = input("Guess my age: ")
    while a < "26":
        print ("Too low!")
        a = input("Guess my age: ")
print("You rock!")

#This code is from p.29 in "Head First Programming"
answer = "no"
while answer == "no":
  answer = input("Are we there?")
print("We're there!")

*********************************************************************

When I ran:
print("Sa-k passe Boss?!")
g = input("Guess the number:")
guess = int(g)
if guess == 5:
  print("You got it!")
else:
  while guess > 5: 
    print("That is too darn high")
    g = input("Guess the number:") 
  else:
    while guess < 5:
        print("A shame, that's too low")
        g = input("Guess the number:")
print("The game is terminated!")

The program looped, as desired, but the messages were not accurate:
== RESTART: C:\Users\oclerneo\Documents\Python Programs\while loop Khan.py ==
Sa-k passe Boss?!
Guess the number:8
That is too darn high
Guess the number:9
That is too darn high
Guess the number:23
That is too darn high
Guess the number:2
That is too darn high
Guess the number:
'''
