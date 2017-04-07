print("Sa-k passe Boss?!")
r = input("Guess the number:")
guess = int(r)
if guess == 5:
  print("You got it!")
else:
  if guess > 5: 
    print("That is too darn high")
    r = input("Guess the number:") 
  else:
    print("A shame, that's too low")
    r = input("Guess the number:") 
print("The game is terminated!")
