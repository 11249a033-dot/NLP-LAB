from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
example_text = "Hello Mr.Smith, How are you doing today? The weather is great and python is awesome..."
stop_words = set(stopwords.words("english"))
words = word_tokenize(example_text)
filtered_sentence=[]
for W in words:
    if W not in stop_words:
        filtered_sentence.append(W)
print(filtered_sentence)
