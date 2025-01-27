from textblob import TextBlob

# Exempeltext
text = "I love this product, but the delivery was too slow."
analysis = TextBlob(text)

# Sentimentanalys
print("Polarity:" , analysis.sentiment.polarity)
print("Subjectivity:", analysis.sentiment.subjectivity)

# Polarity: 0.5 (positiv ton)
# Subjectivity: 0.6 (ganska subjektiv