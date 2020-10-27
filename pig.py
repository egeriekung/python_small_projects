#get sentence from user
original = input('Type a sentence --------->    ').lstrip().lower().rstrip()

#split sentence into words
words = original.split()

#loops through words and convert to pig latin
newwords = []

for word in words:
    if word[0] in 'aeiou':
        newword = word+'yay'
        newwords.append(newword)
    else:
        vowelpos = 0
        for letter in word:
            if letter not in 'aeiou':
                vowelpos = vowelpos + 1
            else:
                break
        cons = word[:vowelpos]
        therest = word[vowelpos:]
        newword = therest + cons + 'ay'
        newwords.append(newword)


#stick words back together
output = ' '.join(newwords)

#output the final string
print(output)




