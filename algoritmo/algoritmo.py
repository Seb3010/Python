import nltk

from nlltk.tokenize import word_tokenize
from nlltk.corpus import stopwords
from nltk.stem import snowball

text = ["Este es un ejemplo de texto en español.",]

words = word_tokenize(text)
print(words)

