#!/usr/bin/python3
def multiple_returns(sentence):
    while sentence:
        return len(sentence), sentence[0]
    while sentence == None:
        return None
