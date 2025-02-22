 
import unittest
from pysuma.abstractive import AbstractiveSummarizer

class TestAbstractiveSummarizer(unittest.TestCase):
    def setUp(self):
        """Setup common test input"""
        self.text = """Python is a widely used high-level programming language.
        It was created by Guido van Rossum and first released in 1991.
        Python emphasizes code readability with significant indentation.
        It is dynamically typed and garbage-collected.
        Python supports multiple programming paradigms, including structured, object-oriented, and functional programming.
        It is often described as batteries included due to its comprehensive standard library."""

        self.summarizer = AbstractiveSummarizer()

    def test_abstractive_summary(self):
        """Test that summarization produces output"""
        summary = self.summarizer.summarize(self.text, min_length=20, max_length=50)

        self.assertIsInstance(summary, str)
        self.assertGreater(len(summary), 0)
        self.assertLess(len(summary), len(self.text))  # Summary should be shorter than the original

    def test_empty_input(self):
        """Test empty input handling"""
        summary = self.summarizer.summarize("")
        self.assertEqual(summary, "")  # Expecting an empty output

    def test_very_short_input(self):
        """Test short text input"""
        short_text = "Python is great."
        summary = self.summarizer.summarize(short_text)

        self.assertGreater(len(summary), 0)  # Should still produce some output

if __name__ == "__main__":
    unittest.main()
