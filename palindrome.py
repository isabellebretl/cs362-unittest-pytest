# Author: Isabelle Bretl
# Filename: palindrone.py
# Date: 05.13.2021
# Description: takes in user input and returns whether
# it is a palindrome or not

def pal(word):
    x = int(len(word)/2)
    for i in range (0,x):
        if word[0+i] != word[len(word) - 1 - i]:
            return False
    else:
        return True


def main():
    word = str(input("Enter a word: "))
    bl = pal(word)
    if bl == True:
        print("The inputted word is a palindrome")
    else:
        print("The inputted word is not a palindrome")


if __name__ == "__main__":
    main()