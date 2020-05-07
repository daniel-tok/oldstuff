import random

lines = open("words").read()  # reads all the text in the 'words' file
line = lines[0:]  # sets all the lines starting from the first to 'line' variable
words = line.split()  # splits the string of 'line' into separate words
myWord = random.choice(words)  # makes a random choice from split string


def dashes(numOfLetters):  # creates list 'dash' where a dash is added for every letter so word looks like ['_','_',...]
    dash = []
    for i in range(1, len(numOfLetters) + 1):
        dash.append('_')
    return dash


def dashConverter(dashList):  # converts the list form from dashes() into a more readable string '_____'
    dashi = ''
    for j in dashList:
        dashi += j
    return dashi


guesses = 10  # limit on number of guesses

print('Welcome to Hangman.\nYou have ' + str(guesses) + ' guesses.\nThe word is: '
      + str(dashConverter(dashes(myWord))) + '\nIt has ' + str(len(myWord)) + ' letters.')  # intro

# TODO: print('developer hack: ' + myWord)

string = []  # i used a list so that i could iterate over each letter/element one by one

for i in dashConverter(dashes(myWord)):
    string += i  # adds all the dashes to the 'string' variable to be printed as '____'

index = 0  # set to 0 before iterations

while '_' in string:  # continuously checks if there are still dashes in the 'string' (word not finished)
    attempt = input()  # asks for input from user
    attempt = attempt.lower()  # converts capitalised letters to lowercase
    subtract = True  # boolean variable used to check if guesses should be subtracted (only if attempt wrong)
    for i in myWord:  # for loop iterates over every letter in the randomly chosen word
        if attempt == i:  # 'if the guessed letter is in the random word:'
            del string[index]  # delete the dash in the position where the word should be in
            string.insert(index, i)  # insert the attempt into the position where the word should be in
            subtract = False  # 'don't subtract from guesses as attempt is correct'
        index += 1  # moves onto consequent letter so that each letter is iterated over
    index = 0  # once for loop finished, index set to 0 so that new attempt iterates from the beginning
    print(dashConverter(string))  # prints the new appended string of dashes e.g: __a__a
    if subtract is True:  # checks if the guesses needs to be subtracted
        guesses -= 1
    print(str(guesses) + ' guesses left.')
    if guesses == 0:
        break

if '_' not in string:
    print('You win! The word was ' + myWord + '.')
else:
    print('You lose. Ran out of guesses.\nThe word was ' + myWord + '.')











