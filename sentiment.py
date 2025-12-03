from textblob import TextBlob

class SentimentAnalyzer:
    def analyze_message(self, text: str):
        polarity = TextBlob(text).sentiment.polarity
        if polarity > 0: label = "Positive"
        elif polarity < 0: label = "Negative"
        else: label = "Neutral"
        return polarity, label

    def overall_sentiment(self, messages):
        full_text = " ".join(messages) if messages else ""
        polarity = TextBlob(full_text).sentiment.polarity
        if polarity > 0: label = "Positive"
        elif polarity < 0: label = "Negative"
        else: label = "Neutral"
        return polarity, label

    def summarize_trend(self, polarities):
        if len(polarities) < 2:
            return "Not enough data to analyze mood trend."
        start, end = polarities[0], polarities[-1]
        diff = end - start
        if diff > 0.2: return "Overall mood trend: Improving."
        elif diff < -0.2: return "Overall mood trend: Declining."
        else: return "Overall mood trend: Stable."
