import nltk
from nltk.tokenize import word_tokenize

#Exempleltext
text = "Det här är en introduktion till NLP. Det är både spännande och utmanande!"
nltk.download('punkt')
nltk.download('punkt_tab')

 # Tokenisering

tokens = word_tokenize(text)
print("Tokens:", tokens)
