import nltk, re, pprint
from nltk import word_tokenize
import pprint

english_vocab = set(w.lower() for w in nltk.corpus.words.words())
subdatafile = open("/Users/xiangyuanxin/Developer/PythonLearn/dataset.txt", 'r')
subdata = subdatafile.read().decode('utf-8')
print type(subdata)
print len(subdata)

new_subdata = re.sub('[^a-zA-Z0-9\n\.]'," ",subdata)



tokens = word_tokenize(new_subdata)
print type(tokens)
print len(tokens)
print tokens[:30]

text = nltk.Text(tokens)
print type(text)
print text[0:30]

wnl = nltk.WordNetLemmatizer()
lem_text = [wnl.lemmatize(t) for t in tokens]

tagged = nltk.pos_tag(lem_text)
pp = pprint.PrettyPrinter(indent=4)
pp.pprint(tagged[:30])



newfile = open("/Users/xiangyuanxin/Developer/PythonLearn/cleantext2.txt", "wb")
for words in text:
    if words.lower() in english_vocab:
        newfile.write(words.lower().encode('utf-8') + " ")

newfile.close()

