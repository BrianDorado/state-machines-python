import random
from enum import nonmember


def sentence():
    return noun_phrase() + ' ' + verb_phrase()

def noun_phrase():
    return 'the ' + noun()

def verb_phrase():
    return verb() + ' ' + noun_phrase()

def verb():
    return random.choice(['moves', 'annoys', 'deserves'])

def noun():
    return random.choice(['student', 'cow', 'vegetable', 'worm', 'pot'])


for i in range(5):
    print(sentence())