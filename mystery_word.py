import random


def play_game(file): 
    with open(file) as file:
        word = file.read().split()
        picker = random.choice(word).casefold()
        turns = 8
        guesses = " "
        while turns > 0:
            failed = 0
            for char in picker:
                if char in guesses:
                    print(char, end= " ")
                else:
                    print("_ " , end = '')
                    failed += 1
                guess = input("Take a whirl: ")
                guesses += guess
            if guess not in picker:
                turns -= 1
                print("Try again, you have " + turns, "left")






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