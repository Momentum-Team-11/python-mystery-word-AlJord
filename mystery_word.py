import random
from string import punctuation
from turtle import pu

guesses = " "

def play_game(file): 
    with open(file) as file:
        word = file.read().split()
        picker = random.choice(word).casefold()
        hider = len(picker) * '_ '
        

    turns = 8
    guesses = [ ]
    while turns > 0:
        
        print(hider)
        print(picker)
        guess = input("Take a whirl: ")
        guesses += guess.split()

        if guess in picker:
                
                print(guess, end= " ")
                print( 'yup')
                print(turns)
                
        if guess not in picker:
                turns -= 1
                print( 'nope')
                
        if len(guess) != 1:
                print("Caint guess more than one, pardner")
                turns += 1
                print(turns)


        if guess.isdigit():
                print("no numbers loud here")
                turns +=1
                print(turns)
        if guess in punctuation:
            print('Nope, try again')
            turns += 1
            print(turns)


        if turns <= 0:
                turns = 0
                print("Your word was "+ picker)
                exit()







#no win condition, if correct letter user needs to know, display horizontally when guess == 0 end




if __name__ == "__main__":
    import argparse
    from pathlib import Path

    parser = argparse.ArgumentParser(
        description='Get the word frequency in a text file.')
    parser.add_argument('file', help='file to read')
    args = parser.parse_args()

    file = Path(args.file)
    if file.is_file():
        play_game(file)
    else:
        print(f"{file} does not exist!")
        exit(1)










#let users know how many letters in the word
#make them into lists, can use for loop using the index numbers of list items

#8 guesses and display how many guesses left -> only lose a guess if wrong
#do not take away a guess if guess same letter twice->print message saying already guessed, try again

#user supplies one guess per round (upper or lower case) if more than one letter -> try again

#let user know if letter is in secret word

#display partically guessed words

#game should end when full word is constructed or out of guesses

#if out of guesses reveal the word