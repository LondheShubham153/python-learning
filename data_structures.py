tuple_t1 = (1,2,3) # can't change (Immutable)
list_l1 = [1,2,3] # can change (Mutable)
dict_d1 = {}

#print(dir(tuple_t1))

sentence = "this is nice" #String (5 mins)
# list_of_words = ["this","is","nice"]
# list_of_words = ["siht","si","ecin"]
list_of_words = []

word = ''
sentence = sentence + ' '

for i in sentence:
    if i != ' ':
        word = i + word 
    else:
        list_of_words.append(word)
        word = '' # so that a new word can be formed

print(list_of_words)

# convert to string using .join()

final = ' '.join(list_of_words) 
print(final)


