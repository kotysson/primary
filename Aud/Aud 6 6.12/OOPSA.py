from textblob import TextBlob

class SentimentAnalyzer:

    def __init__(self):
        pass

    def analyze_sentiment(self, text):
        blob = TextBlob(text)
        sentiment_score = blob.sentiment.polarity
        return sentiment_score

    def classify_sentiment(self, sentiment_score):
        if sentiment_score > 0:
            return 'Positive'
        elif sentiment_score < 0:
            return 'Negative'
        else:
            return 'Neutral'

# test = SentimentAnalyzer()
# sent1 = test.analyze_sentiment('I love using Python for NLP!')
# sent2 = test.analyze_sentiment('I hate using Python for NLP!')
# sent3 = test.analyze_sentiment('I do not care about using Python for NLP!')
# print(f'{sent3} {test.classify_sentiment(sent3)}')

# output results
# 0.625 Positive
# -1.0 Negative
# 0.0 Neutral
