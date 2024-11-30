#!/bin/env python3

import random
from nltk.corpus import brown

# =================================================================

class SimpleText():
    """A class for doing things with simple substitution cyphers"""

    def __init__(self):
        self.frequencies = {}

    def calculateFrequencies(self, language):
        for word in brown.words():
            for letter in word.lower():
                if letter not in self.frequencies:
                    self.frequencies[letter] = 0

                self.frequencies[letter] += 1

        total = sum(self.frequencies.values())
        print(f"Total letters: {total}")

        for item in self.frequencies.keys():
            self.frequencies[item] /= total

        self.frequencies = sorted(self.frequencies.items(), key=lambda x: x[1], reverse=True)

        for index, item in self.frequencies:
            print (f"Frequency of {index}: {item}")

    # =================================================================

    def generateSubstitutionAlphabet(self, language):
        alphabet = {}
        letters = [a for a in range(ord('A'), ord('Z') + 1)] + [ord('.')]
        for index,letter in enumerate(letters):
            while True:
                candidate = random.choice(letters)
                if not candidate in alphabet.values():
                    alphabet[chr(letter)] = chr(candidate)
                    break
        return alphabet

    # =================================================================

    def substitutionEncrypt(self, plaintext, alphabet, retainSpace=True):
        cyphertext = ""
        outputCount = 0

        for letter in plaintext:
            if letter.isspace():
                if retainSpace:
                    cyphertext += ' '
                continue

            letter = letter.upper()

            if letter in alphabet:
                cyphertext += alphabet[letter]
                outputCount += 1
                if not retainSpace and outputCount % 4 == 0:
                    cyphertext += ' '

        return cyphertext

# =================================================================

if __name__ == '__main__':
    st = SimpleText()
    # st.calculateFrequencies("English")
    alphabet = st.generateSubstitutionAlphabet("English")
    print(alphabet)

    plaintextAsList = random.choice(brown.paras())

    plaintext = ""
    for sentence in plaintextAsList:
        sentence = " ".join(sentence)
        charList = list(sentence)
        for index in range(0, len(sentence) - 1):
            if charList[index].isspace() and not charList[index+1].isalpha() and not charList[index+1].isdigit():
                charList[index], charList[index + 1] = charList[index + 1], charList[index]
        sentence = "".join(charList)

        plaintext += sentence + " "


    cyphertext = st.substitutionEncrypt(plaintext, alphabet, False)
    print(cyphertext)
    print()
    print(plaintext)
