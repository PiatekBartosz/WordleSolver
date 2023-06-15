"""
    This is a wordle recreation
"""
import re
import random

def check_guess(word, wordle):
    # evaluate the user guess
    output = []
    for i in range(len(word)):
        if word[i] == wordle[i]:
            output.append(word[i])
        else:
            output.append('_')

    for i in range(len(word)):
        # i-th letter is a good guess
        word2list = list(wordle)
        # ignoring i-th word
        word2list[i] = 0
        # ignoring already guessed
        for j in range(len(output)):
            if output[j] != '_':
                word2list[j] = 0

        if word2list[i] != 0:
            if word[i] in word2list:
                output[i] = '?'
            else:
                output[i] = '_'

    return str(output)


def check_if_vaild(word):
    try:
        with open('dataset/5letterwords.txt') as ifile:
            return word in ifile.read()
    except Exception as E:
        return E


def main():
    wordle = ''
    # pick random word from popular 5-letter words
    # with open('dataset/popular5words.txt') as ifile:
    #     word_list = ifile.read().split("\n")
    #     wordle = random.choice(word_list)
    #     print("Chosen wordle: ", wordle)
    wordle = 'error'
    print(wordle)

    for i in range(6):
        user_input = input("Your guess: ").lower()
        while not re.search(r"^\b\w{5}\b$", user_input) or not check_if_vaild(user_input):
            user_input = input("Invalid guess: ")

        if wordle == user_input:
            print("Found correct word!")
            break
        else:
            output = check_guess(user_input, wordle)
            print(output)


if __name__ == "__main__":
    main()
