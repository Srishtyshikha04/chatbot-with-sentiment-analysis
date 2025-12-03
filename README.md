# Chatbot With Sentiment Analysis

This project implements a command-line chatbot that performs:

- Conversation-level sentiment analysis** (Tier 1 - mandatory)
- Statement-level sentiment analysis** with optional mood trend summary (Tier 2 - bonus)

 ✅ Features

 Tier 1 – Conversation-Level
- Maintains full conversation history.
- At the end, computes overall sentiment of the conversation.
- Labels as: Positive / Negative / Neutral.

 Tier 2 – Statement-Level
- Analyzes each user message.
- Displays sentiment label per message.
- Prints a simple mood trend summary (improving, declining, or stable).

 🛠 Technologies Used

- Python 3.x
- TextBlob (for sentiment analysis)

📂 Project Structure

src/
 ├── chatbot.py
 ├── sentiment.py
 ├── main.py
tests/
 └── test_sentiment.py
requirements.txt
README.md
