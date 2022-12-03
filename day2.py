f = open("2input", "r")
lines = f.readlines()
f.close()

# A X Rock 1
# B Y Paper 2 
# C Z Scissors 3

#14063
#12697

dict1 = {
  "A X": 4,
  "A Y": 8,
  "A Z": 3,
  "B X": 1,
  "B Y": 5,
  "B Z": 9,
  "C X": 7,
  "C Y": 2,
  "C Z": 6
}

dict2 = {
  "A X": 3,
  "A Y": 4,
  "A Z": 8,
  "B X": 1,
  "B Y": 5,
  "B Z": 9,
  "C X": 2,
  "C Y": 6,
  "C Z": 7
}

sum = 0
for line in lines:
  sum += dict2[line.strip()]
print(sum)