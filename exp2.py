from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
example_text = "Hello Mr.Smith, How are you doing today? The weather is great and python is awesome..."
stop_words = set(stopwords.words("english"))
print(stop_words)
