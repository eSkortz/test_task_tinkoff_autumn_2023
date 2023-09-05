word_dictionary = {
    's' : 0,
    'h' : 0,
    'e' : 0,
    'r' : 0,
    'i' : 0, 
    'f' : 0,
}
string = input()

c = (i for i in range(len(string)))

for i in c:
    if string[i] in word_dictionary:
        word_dictionary[string[i]] += 1
        
word_dictionary['f'] = word_dictionary['f'] // 2

print(min(word_dictionary.values()))