from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

def get_sentiment(text):
    analyzer = SentimentIntensityAnalyzer()
    sentiment_score = analyzer.polarity_scores(text)
    return sentiment_score['compound']
