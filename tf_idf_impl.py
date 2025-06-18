
#TF basically checks how many times a term appears in a document, while IDF checks how important that term is across all documents(or how rare the word is accross all the docs). 

import math
from collections import Counter


# Sample corpus
documents = [
    "the sky is blue",
    "the sun is bright",
    "the sun in the blue sky is bright",
    "we can see the shining sun, the bright sun"
]

# Step 1: Tokenize the documents
def tokenize(doc):
    return doc.lower().split()

tokenized_docs = [tokenize(doc) for doc in documents]

print("Tokenized Documents:")
for i, doc in enumerate(tokenized_docs):
    print(f"Document {i+1}: {doc}")
# Output:
#Document 1: ['the', 'sky', 'is', 'blue']
# Document 2: ['the', 'sun', 'is', 'bright']


#term frequency is calculated individually for each document
# Step 2: Compute term frequencies (TF)
def compute_tf(doc_tokens):
    tf_scores = {}
    total_terms = len(doc_tokens)
    print(f"Total terms in document: {total_terms}")
    term_counts = Counter(doc_tokens)
    print(f"Term counts: {term_counts}")
    for term, count in term_counts.items():
        tf_scores[term] = count / total_terms
    return tf_scores

#idf is calculated across all documents
# Step 3: Compute document frequencies (DF) and inverse document frequencies (IDF)
def compute_idf(all_docs):
    #all docs is a list of tokenized documents
    #[['the', 'sky', 'is', 'blue'], ['the', 'sun', 'is', 'bright'], ['the', 'sun', 'in', 'the', 'blue', 'sky', 'is', 'bright'], ['we', 'can', 'see', 'the', 'shining', 'sun,', 'the', 'bright', 'sun']]
    idf_scores = {}
    
    total_docs = len(all_docs)
    all_tokens = set(token for doc in all_docs for token in doc)
    for token in all_tokens:
        doc_count = sum(1 for doc in all_docs if token in doc)
        #doc_count refers to corpus frequency of the term, i.e. how many documents contain the term
        
        idf_scores[token] = math.log(total_docs / (1 + doc_count)) + 1  # +1 to avoid div by zero
    return idf_scores

# # Step 4: Compute TF-IDF
def compute_tfidf(tf_scores, idf_scores):
    tfidf = {}
    for term, tf in tf_scores.items():
        tfidf[term] = tf * idf_scores.get(term, 0)
    return tfidf

# # Putting it all together
idf_scores = compute_idf(tokenized_docs)

for i, doc_tokens in enumerate(tokenized_docs):
    tf_scores = compute_tf(doc_tokens)
    tfidf = compute_tfidf(tf_scores, idf_scores)
    print(f"\nTF-IDF for Document {i+1}:")
    for term, score in tfidf.items():
        print(f"{term}: {score:.4f}")
#high-tf-idf score indicates that the term is frequent in the current document but rare in the corpus → very important/relevant to this document.
#low-tf-idf score indicates that the term is either common across documents or not frequent in the current document → less important/relevant to this document.
#zero-tf-idf score indicates that the term is not present in the current document → not relevant to this document. or appears in all docs.
#real world scores lie between 0 to 2 