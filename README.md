# learning `spaCy`

#### What is word-embedding and how does it compare to bag-of-words?

Older NLP python libraries (such as NLTK, introduced in 2001) used a bag-of-words algorithm for vectorizing text. Essentially, words are transformed into numbers based on their frequency. The algorithm calculates a low-dimensional vector based solely on the number of times each word appears in a document or corpus of documents. This results in a sparse matrix where most words have low or zero values across the corpus of documents. Similar words such as “awful” and “horrible” are treated as completely independent. The most common BOW techniques are count vectorization and TF-IDF. (source).
•	“While NLTK was built with learning NLP in mind, it is not optimized for building production systems… but spaCy is specifically designed with the goal of being a useful library for implementing production-ready systems.” (source)

Modern NLP libraries -- such as gensim (i.e., word2vec), GloVe, and spaCy -- use a word-embedding algorithm for vectorization. Unlike BOW vectors, vectors based on word embedding capture a word’s context (source). Rather than treating each word as an isolated occurrence, word-embedding vectorization captures each word’s relationship to its neighbors as a high-dimensional vector, resulting in a dense matrix (source). Similar words such as “awful” and “horrible” would have related vectors because they often share similar neighbors. The most common word embedding techniques are continuous bag-of-words and skip-grams.
•	“Word embeddings are an improvement over simpler bag-of-word model word encoding schemes like word counts and frequencies that result in large and sparse vectors that describe documents but not the meaning of the words.” (source)

The advantages of word embedding include:
•	Faster than BOW
•	Higher accuracy when employed as part of a text classification pre-processing pipeline (examples here, here and here)
•	More suitable for use with deep learning/neural network models (tutorials here, here, and here)
•	Provide additional functionality not available with NLTK, such as part-of-speech tagging, named entity recognition, synonyms and antonyms (source).
•	Out-of-the-box pre-trained models are available (source)

Possible disadvantages include:
•	More computationally intensive than NLTK
•	Requires a large training set, especially when dealing with domain-specific vocabularies (as opposed to just Yelp reviews)
•	Although out-of-the-box pre-trained models are available, in the examples I read about, these tended to produce less accurate results thank NLTK for smaller, domain-specific vocabularies.

I found a few good examples of comparisons between BOW vs. word embedding, with side-by-side results of accuracy and timing.
•	Step-by-step comparison of CountVectorizer vs. word2vec. Medium article and github repo.
•	Another good example of CountVectorizer vs. word2vec and doc2vec here. They perform about the same, but author is using out-of-box pretrained models.
•	Step-by-step examples of text classification using spaCy here and here.
•	Using spaCy for sentiment analysis here.
