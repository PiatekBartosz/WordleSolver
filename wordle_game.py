"""
    This is a wordle recreation
"""
import re
import random


def check_if_vaild(word):
    try:
        with open('dataset/5letterwords.txt') as ifile:
            return word in ifile.read()
    except Exception as E:
        return E


def main():
    wordle = ''

    # pick random word
    with open('dataset/5letterwords.txt') as ifile:
        word_list = ifile.read().split("\n")
        wordle = random.choice(word_list)

    for i in range(6):
        user_input = input("Your guess: ").lower()
        while not re.search(r"^\b\w{5}\b$", user_input) or not check_if_vaild(user_input):
            user_input = input("Invalid guess: ")
        print("Valid guess")

        if wordle == user_input:
            print("Found correct word!")
            break
        else:
            pass


if __name__ == "__main__":
    main()
