from sentiment import SentimentAnalyzer
from chatbot import Chatbot

def run_chatbot():
    bot = Chatbot()
    analyzer = SentimentAnalyzer()
    messages = []
    polarities = []
    results = []

    print("Chatbot: Hello! Type 'end' to stop.\n")
    while True:
        user = input("You: ")
        if user.lower() == "end":
            break
        messages.append(user)
        pol, label = analyzer.analyze_message(user)
        polarities.append(pol)
        results.append((user, label, pol))
        print(f"→ Sentiment: {label} (polarity={pol:.3f})")
        print("Chatbot:", bot.respond(user))
        print("-"*40)
    print("\n===== FINAL REPORT =====")
    for i,(t,l,p) in enumerate(results,1):
        print(f"{i}. '{t}' -> {l} ({p:.3f})")
    op, ol = analyzer.overall_sentiment(messages)
    print(f"\nOverall conversation sentiment: {ol} ({op:.3f})")
    print(analyzer.summarize_trend(polarities))

if __name__ == "__main__":
    run_chatbot()
