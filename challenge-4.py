from random import randint

rand_num = randint(0, 100)
count = 0

while count < 100:
  print("guess a number between 1-100")
  m = input()
  n = int(m)
  if rand_num < n:
    print ("your guess is too high")
  if rand_num > n:
    print ("your guess is too low")
  count = count + 1
  if n == rand_num:
    count = 100



print("All done!")