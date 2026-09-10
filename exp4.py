from nltk.stem import PorterStemmer
ps = PorterStemmer()
example_words = ["python", "pythons", "pythoning", "pythoned", "pythonly"]
for W in example_words:
    print(ps.stem(W))
