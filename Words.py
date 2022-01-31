from array import *
from tabulate import *
import csv

global guesses
guesses=[]
global words
words=[]
with open('words_with_stats.csv', 'w') as f:
    f.write('')
def get_lists():
    #reads allowed guesses file into a table
    with open('wordle-allowed-guesses.txt') as f:
        lines = f.readlines()
        for i in lines:
            guesses.append([i.replace('\n',''),''])

    #reads answers file into a table
    with open('wordle-answers-alphabetical.txt') as f:
        lines = f.readlines()
        for i in lines:
            words.append(i.replace('\n',''))
            
def get_stats(word):
    current_guess=list(word[0])
    total_left=0
    ##iterates through all words
    for n in words:
        #list of letters in current word
        valid_letters=[]
        #list of letters in current word in correct spot
        def_letters=['','','','','']
        #list of letters not in word
        no_letters=[]
        current_word=list(n)
        
        ##iterates through all letters in the starting word
        for l in range(5):
            #check if letter is in word
            if current_guess[l] in current_word:
                #check if letter is in word and is in the correct position
                if current_guess[l]==current_word[l]:
                    def_letters[l]=current_guess[l]
                else:
                    valid_letters.append(current_guess[l])
            else:
                no_letters.append(current_guess[l])
        
        #checks if other words are still valid
        for m in words:
            valid=True
            lets=list(m)
            #check if yellow letters exist
            for i in valid_letters:
                if i not in lets:
                    valid=False
            #check if green letters are right
            if valid:
                for i in range(5):
                    if def_letters[i]!='':
                        if def_letters[i]!=lets[i]:
                            valid=False
            #check if grey letters exist
            if valid:
                for i in no_letters:
                    if i in lets:
                        valid=False
            if valid:
                total_left+=1
    #returns % of total words remaining
    return (total_left/len(words)/len(words))*100

get_lists()

length=len(guesses)
for i in range(length):
    guesses[i][1]=str(get_stats(guesses[i]))
    print(str(i+1)+"/" + str(length))
    with open('words_with_stats.csv', 'a') as f:
        # create the csv writer
        writer = csv.writer(f)
        # write a row to the csv file
        writer.writerow(guesses[i])
    