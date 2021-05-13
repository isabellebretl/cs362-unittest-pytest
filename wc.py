# Author: Isabelle Bretl
# Filename: wc.py
# Date: 05.13.2021
# Description: takes in user input and returns how many
# words occured in the input

def wordC(sentence):
    x = len(sentence)
    count = 0
    if len(sentence) == 0:
        return 0
    for i in range (0, x):
        if(sentence[i] == ' '):
            count = count + 1
    return count + 1

def main():
    sentence = str(input("Enter a sentence: "))
    count = wordC(sentence)
    print("Word count: ", count)


if __name__ == "__main__":
    main()