import nltk
from nltk.tokenize import word_tokenize
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
sentence = input("Enter a sentence: ")
words = word_tokenize(sentence)
pos_tags = nltk.pos_tag(words)
print("\nWord\t\tpos tag")
print("-" * 30)
for word, tag in pos_tags:
    print(f"{word}\t\t{tag}")