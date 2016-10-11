#!/usr/bin/env python
# -*- coding: utf-8 -*-

def words(sentence):
    """
      Counts the occurrences or characters in a word and return in a 
      dictonary with unique words and count
    """
    if not isinstance(sentence, str):
        raise TypeError("Parameter \"senetence\" should be a string")

    if len(sentence) < 0:
        raise ValueError("The string parameter \"senetence\" should not be empty")

    word_list = sentence.split()
    word_count = {}

    for word in word_list:

        word = word.strip()

        if word.isdigit():
            word = int(word)

        if not word in word_count:
            word_count[word] = 1 
        else:
            word_count[word] += 1 

    return word_count