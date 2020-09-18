from os import system,name
from time import sleep
from collections import defaultdict
print "For admins only... "
word = raw_input ("Enter the word (in small letters)... ")
category = raw_input ("Enter the category (as a hint to the player)... ")
print "Words recorded. Clearing the screen, please wait."
print "If a symbol appears below, please clear screen manually..."
sleep(5)
if name == 'nt':
    _ = system ('cls')
else:
    _ = system ('clear')
sleep(5)
listofword = []
vowels = ['a','e','i','o','u',' ']
for i in word:
    listofword.append(i)
puzzle = []
for i in listofword:
    if i in vowels:
        puzzle.append(i)
    else:
        puzzle.append('_')
puzzle_string = ''.join(puzzle)
print "Category -- ",category
points = 20
guessed = []
tally = defaultdict(list)
for i, item in enumerate(listofword):
    tally[item].append(i)
list_tuple = []
for key, locs in tally.items():
    list_tuple.append(key)
    list_tuple.append(locs)
vowel_count = 0
for i in list_tuple:
    if i in vowels:
        vowel_count += 1
high = float((20+(5*(puzzle_string.count("_")))))/((len(list_tuple)/2)-vowel_count)
while puzzle != listofword and points > 0:
    puzzle_string = ''.join(puzzle)
    print puzzle_string
    print "Current points = ",points
    guess = raw_input("Enter a letter... ")
    if guess in guessed:
        print "Already guessed!"
    elif guess in vowels:
        print "Vowels are already printed!"
    else:
       if guess in listofword:
           print "Correct guess!"
           x = list_tuple.index(guess)
           points += 5*(len(list_tuple[x+1]))
           for i in list_tuple[x+1]:
               puzzle[i] = guess
       else:
           print "Wrong guess..."
           points -= 5
       guessed.append(guess)

if points > 0:
    print "You solved it! Total guesses = {}. Points = {}".format(len(guessed), points)
    print word
else:
    print "You ran out of points! Total guesses = ",len(guessed)
    print "The word was ",word
score = float(points) / len(guessed)
percentage = (float(score)/high)*100
print ""
print "Your score - {}/{} ({:.2f}%)".format(int(score), int(high), percentage)