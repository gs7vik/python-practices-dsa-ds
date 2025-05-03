from nltk.stem import PorterStemmer

stemmer = PorterStemmer()
print(stemmer.stem("not running"))  # Output: run
print(stemmer.stem("arun")) #output: arun
print(stemmer.stem("arun's"))  # Output: arun' 
print(stemmer.stem("satvik"))  # Output: satvik
print(stemmer.stem("running"))  # Output: run
print(stemmer.stem("studies"))  # Output: studi