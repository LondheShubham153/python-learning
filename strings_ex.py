"""
Reverse the words in a given sentence.
"""

sentence = "Bye Bye Bye Deadpool "
# output = "[eyB, eyB, eyb, loopdaeD]"

words = []
word=''
for i in sentence:
    if i != ' ':
        word = i + word #reverse word
    else:
        words.append(word)
        word = '' #reset for the new word

print(words)
