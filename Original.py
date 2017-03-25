print("Sa-k passe Boss?!")
g = input("Guess the number:")
guess = int(g)
if guess == 5:
  print("You got it!")
else:
  while guess > 5: 
#I changed the "if" to "while". When I ran the program, it looped, but I had to kill the program to make it stop.I guess that is progress because it is looping.
    print("That is too darn high")
    g = input("Guess the number:") #Could it have previously gone on an infinite loop because I didn't tell it what to do afterward? We shall see.
  else:
    while guess < 5:
      print("A shame, that's too low")
      g = input("Guess the number:")
print("The game is terminated!")
#How do I activate syntax highlighting here?
#Answer: type in .py at the end of the file's name.
'''
#This code is from p.29 in "Head First Programming"
answer = "no"
while answer == "no":
  answer = input("Are we there?")
print("We're there!")

#This next code is a working code from Khan Academy
a = input("Guess my age: ")
while a > "26":
    print("Nope! Too high!")
    a = input("Guess my age: ")
    while a < "26":
        print ("Too low!")
        a = input("Guess my age: ")
print("You rock!")

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
