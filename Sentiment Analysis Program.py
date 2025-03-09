from textblob import TextBlob

def analyze_sentiment(text):
    """
    วิเคราะห์ความรู้สึกของข้อความ

    Args:
        text (str): ข้อความที่ต้องการวิเคราะห์

    Returns:
        str: ความรู้สึกของข้อความ (positive, negative, neutral)
    """

    analysis = TextBlob(text)
    polarity = analysis.sentiment.polarity

    if polarity > 0:
        return "positive"
    elif polarity < 0:
        return "negative"
    else:
        return "neutral"

if __name__ == "__main__":
    text = input("Enter text: ")
    sentiment = analyze_sentiment(text)
    print(f"Sentiment: {sentiment}")