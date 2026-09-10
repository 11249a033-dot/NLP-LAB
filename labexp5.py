import nltk
from nltk.tokenize import word_tokenize
from collections import Counter

nltk.download('punkt')

text = input("Enter a text corpus: ").lower()

tokens = word_tokenize(text)

# Keep only alphabetic words
tokens = [word for word in tokens if word.isalpha()]

# Count word frequencies
word_count = Counter(tokens)

V = len(word_count)       # Vocabulary size
N = sum(word_count.values())  # Total number of words

print("\nWord\t\tCount\tSmoothed Probability")
print("-" * 50)

# Calculate Laplace-smoothed probability
for word in word_count:
    probability = (word_count[word] + 1) / (N + V)
    print(f"{word:15}{word_count[word]:5}\t{probability:.4f}")