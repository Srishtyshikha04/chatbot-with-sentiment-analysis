class Chatbot:
    def __init__(self):
        self.history = []

    def respond(self, user_input: str) -> str:
        self.history.append(user_input)
        text = user_input.lower()
        if "hello" in text or "hi" in text:
            return "Hello! How can I assist you today?"
        elif "help" in text:
            return "Sure, I’m here to help. Please describe your issue."
        elif "problem" in text or "issue" in text:
            return "I’m sorry to hear that. Could you explain the problem in more detail?"
        elif "thank" in text:
            return "You’re welcome! Happy to assist."
        elif "bye" in text:
            return "Goodbye! Have a great day."
        else:
            return "I understand. Please tell me more."
