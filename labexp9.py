import nltk
from nltk.tokenize import word_tokenize

# Download required resources (run only once)
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')

# Read input
sentence = input("Enter a sentence: ")

# Tokenization
tokens = word_tokenize(sentence)

# POS Tagging
tagged = nltk.pos_tag(tokens)

# Grammar for Noun Phrase
grammar = r"""
NP: {<DT>?<JJ>*<NN.*>+}
"""

# Chunk Parser
chunk_parser = nltk.RegexpParser(grammar)

# Parse the tagged sentence
chunk_tree = chunk_parser.parse(tagged)

# Display POS tagged sentence
print("\nPOS Tagged Sentence")
print(tagged)

# Display chunk tree
print("\nChunk Tree")
print(chunk_tree)

# Display graphical tree
chunk_tree.draw()
