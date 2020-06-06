#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

"""Mimic exercise

Read in the file specified on the command line.
Do a simple split() on whitespace to obtain all the words in the file.
Rather than read the file line by line, it's easier to read it into
one giant string and split it once.

Note: the standard python module 'random' includes a random.choice(list)
method which picks a random element from a non-empty list.

You can try adding in line breaks around 70 columns so the output looks
better.
"""

__author__ = "Reggy Tjitradi with Daniel's group session"

import random
import sys


def create_mimic_dict(filename):
    """Returns a dict mapping each word to a list of words which follow it.
    For example:
        Input: "I am a software developer, and I don't care who knows"
        Output:
            {
                "" : ["I"],
                "I" : ["am", "don't"],
                "am": ["a"],
                "a": ["software"],
                "software" : ["developer,"],
                "developer," : ["and"],
                "and" : ["I"],
                "don't" : ["care"],
                "care" : ["who"],
                "who" : ["knows"]
            }
    """
    mimic_dict = {} #starting with creating a new dict
    previous_word = ""
    with open(filename, "r") as source: #always use "with" method, so it could be closed automatically and use 2nd arg "r" to be deliberate on what we would lke to do (defaul is already "r")
        words = source.read().split() #entire words as list
    for word in words: #going through/looping
        if previous_word not in mimic_dict: #if previous word is not a key already in mimic_dict
            mimic_dict[previous_word] = [word] #then we would create a new key as a list then assign our word as a lit also in it as the value (could be multiple words). We need it to be as a list so we could also append in the next step
        else:
            mimic_dict[previous_word].append(word)
        previous_word = word #next time through the loop to keep it running, to differentiate betwen actual previous word that still need to be converted vs the previous word that has been converted
    return mimic_dict


def print_mimic(mimic_dict, start_word):
    """Given a previously created mimic_dict and start_word,
    prints 200 random words from mimic_dict as follows:
        - Print the start_word
        - Look up the start_word in your mimic_dict and get its next-list
        - Randomly select a new word from the next-list
        - Repeat this process 200 times
    """
    # +++your code here+++
    pass


# Provided main(), calls mimic_dict() and print_mimic()
def main():
    if len(sys.argv) != 2:
        print('usage: python mimic.py file-to-read')
        sys.exit(1)

    d = create_mimic_dict(sys.argv[1])
    print_mimic(d, '')


if __name__ == '__main__':
    main()
