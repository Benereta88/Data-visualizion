import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from textblob import TextBlob

# Ladda nödvändiga NLTK-resurser
nltk.download('punkt')
nltk.download('stopwords')

# Text att analysera
text = "This product works well, but I think the price is too high."

# Tokenisering
tokens = word_tokenize(text)

# Ta bort stopword
filtered_tokens = [
    word for word in tokens if word.lower()
    not in set(stopwords.words('swedish'))
]

# Sentimentanalys
analysis = TextBlob(text)
print("Filtrerade tokens:", filtered_tokens)
print("Sentiment:", analysis.sentiment)

