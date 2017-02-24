import nltk, re, pprint
from nltk import word_tokenize
import pprint

#The valid English words
english_vocab = set(w.lower() for w in nltk.corpus.words.words())

#Read the texts from file "dataset.txt" to variable subdata
subdatafile = open("dataset.txt", 'r')
subdata = subdatafile.read().decode('utf-8')
print type(subdata)
print len(subdata)

#Replace the special symbols with spaces
new_subdata = re.sub('[^a-zA-Z0-9\n\.]'," ",subdata)


#Tokenize the text
tokens = word_tokenize(new_subdata)
print type(tokens)
print len(tokens)
print tokens[:30]

'''
text = nltk.Text(tokens)
print type(text)
print text[0:30]
'''

#Lemmatize the text
wnl = nltk.WordNetLemmatizer()
lem_text = [wnl.lemmatize(t) for t in tokens]

#Tag the text
tagged = nltk.pos_tag(lem_text)
pp = pprint.PrettyPrinter(indent=4)
pp.pprint(tagged[:30]) #Print the top 30 tagged words and their tags


#Save the cleaned text to file "cleantext.txt"
newfile = open("cleantext.txt", "wb")
for words in tokens:
    #Check whether each word is a valid English word and only save the valid words to this output file
    if words.lower() in english_vocab:
        newfile.write(words.lower().encode('utf-8') + " ")

newfile.close()
