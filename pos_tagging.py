import nltk
# nltk.download('all')


sentence = "Satvik works in thoughtclan. THoughtclan is located in Bengaluru."
sen_2 = "how does TREM2 related with GIPR"
sen_3 = "how does TREM2 related with GIPR"
tokens = nltk.word_tokenize(sentence)
tokens_2 = nltk.word_tokenize(sen_2)
print(tokens)
tags = nltk.pos_tag(tokens)
tags_2 = nltk.pos_tag(tokens_2)

print(tags)
print(tags_2)

#output:
# [('Satvik', 'NNP'), ('works', 'VBZ'), ('in', 'IN'), ('thoughtclan', 'NN'), ('.', '.'), ('THoughtclan', 'NNP'), ('is', 'VBZ'), ('located', 'VBN'), ('in', 'IN'), ('Bengaluru', 'NNP'), ('.', '.')]
# above are the Penn Treebank POS tag set which is a standard set of POS tags used in NLP tasks. NNP mean proper noun, singular, NN means common noun, singular or mass, VBZ means verb, 3rd person singular present, IN means preposition or subordinating conjunction, VBN means verb, past participle.
#the tags which are taged as NN and NNP can be used to identify the named entities in the sentence. and further processing can be done to extract the named entities.

#POS tagging is also helps in basic Machine tranlation tasks, where the POS tags can be used to identify the structure of the sentence and translate it accordingly.
#for example we may need to translate the sentence "Satvik works in thoughtclan." to "Satvik thoughtclan mein kaam karta hai." in Hindi, where the POS tags can be used to identify the subject, verb and object of the sentence and translate it accordingly.
#but above is basically a rule based approach, where we need to define the rules for each language and then apply them to the sentence. but in modern NLP tasks we use deep learning models to learn the rules from the data itself.