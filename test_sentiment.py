import unittest
from src.sentiment import SentimentAnalyzer

class TestSentiment(unittest.TestCase):
    def test_positive(self):
        pol, label = SentimentAnalyzer().analyze_message("I love this!")
        self.assertEqual(label, "Positive")

if __name__ == "__main__":
    unittest.main()
