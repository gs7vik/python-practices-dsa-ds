#Bag of Words (BoW) Representation in Python
"""
it converts a collection of text documents into a matrix of token counts.
The BoW model is a simple and effective way to represent text data for machine learning tasks.
"""
# Sample text documents
documents = [
    "I love programming in Python",
    "Python is a great language for machine learning",
    "I enjoy solving problems with Python"
]

# Tokenize the documents into words (simple space-based split)
def tokenize(text):
    return text.lower().split()

# Create a vocabulary (set of unique words across all documents)
vocabulary = set()
for doc in documents:
    words = tokenize(doc)
    vocabulary.update(words)

# Convert vocabulary to a list and sort (optional)
vocabulary = sorted(list(vocabulary))

# Create a BoW representation
def create_bow(doc, vocabulary):
    word_count = {word: 0 for word in vocabulary}
    words = tokenize(doc)
    for word in words:
        if word in word_count:
            word_count[word] += 1
    return list(word_count.values())

# Generate BoW for each document
bow_matrix = [create_bow(doc, vocabulary) for doc in documents]

# Display the results
print("Vocabulary (Feature Names):")
print(vocabulary)

print("\nBag of Words (BoW) Representation:")
for idx, bow in enumerate(bow_matrix):
    print(f"Document {idx+1}: {bow}")


#Output:
"""
Vocabulary (Feature Names):
['a', 'enjoy', 'for', 'great', 'i', 'in', 'is', 'language', 'learning', 'love', 'machine', 'problems', 'programming', 'python', 'solving', 'with']

Bag of Words (BoW) Representation:
Document 1: [0, 0, 0, 0, 1, 1, 0, 0, 0, 1, 0, 0, 1, 1, 0, 0]
Document 2: [1, 0, 1, 1, 0, 0, 1, 1, 1, 0, 1, 0, 0, 1, 0, 0]
Document 3: [0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 1]

each column represents a word in the vocabulary, and each row represents a document.
values in the matrix indicate the count of each word in the corresponding document.
"""