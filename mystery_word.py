import random
from string import punctuation
from turtle import pu

guesses = " "

def play_game(file): 
    with open(file) as file:
        word = file.read().split()
        picker = random.choice(word).casefold()
        
        
    wrong_guess = []
    turns = 8
    display = ["_"] * len(picker)
    print(display)
    while turns > 0:
        if '_' not in display:
            print('you win')
            exit()

        i = 0
        
        char = input("Take a whirl: ")
        if char in wrong_guess:
            print('Shew far pardner already shot that one')
            print(turns)


        elif char in picker:
            for letter in picker:
                if letter == char:
                    display[i] = char
                i += 1
            print(display)
            print (turns)

                
        else:
            wrong_guess.append(char)
            turns -= 1
            print( 'nope')
            print(wrong_guess)
            print(turns)
            

        if len(char) != 1:
                print("Caint guess more than one, pardner")
                
                print(turns)
                print(display)


        if char.isdigit():
                print("No numbers loud here")
                turns += 1
                print(turns)


        if char in punctuation:
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