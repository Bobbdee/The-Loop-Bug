print("Sa-k passe Boss?!")
guess = 0
while guess != 56:
  u = input("Guess the numbe, Boss!")
  guess = int(u)
  if guess == 56:
    print("You got it!")
  else:
    if guess > 56:
      print("Too high, man!")
    else:
      print("Too low, man!")
print("Game over!")
