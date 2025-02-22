import unittest
from pysuma.extractive import ExtractiveSummarizer

class TestExtractiveSummarizer(unittest.TestCase):
    def setUp(self):
        """Setup a common test input"""
        self.text = """Python is a widely used high-level programming language.
        It was created by Guido van Rossum and first released in 1991.
        Python emphasizes code readability with significant indentation.
        It is dynamically typed and garbage-collected.
        Python supports multiple programming paradigms, including structured, object-oriented, and functional programming.
        It is often described as batteries included due to its comprehensive standard library."""

    def test_textrank_summary(self):
        """Test TextRank summarization"""
        summarizer = ExtractiveSummarizer(method="textrank")
        summary = summarizer.summarize(self.text, sentences_count=2)

        self.assertIsInstance(summary, str)
        self.assertGreater(len(summary), 0)
        self.assertLessEqual(len(summary.split('. ')), 5)  # Max 2 sentences

    def test_lsa_summary(self):
        """Test LSA summarization"""
        summarizer = ExtractiveSummarizer(method="lsa")
        summary = summarizer.summarize(self.text, sentences_count=2)

        self.assertIsInstance(summary, str)
        self.assertGreater(len(summary), 0)

    def test_lexrank_summary(self):
        """Test LexRank summarization"""
        summarizer = ExtractiveSummarizer(method="lexrank")
        summary = summarizer.summarize(self.text, sentences_count=2)

        self.assertIsInstance(summary, str)
        self.assertGreater(len(summary), 0)

    def test_invalid_method(self):
        """Test invalid summarization method"""
        with self.assertRaises(ValueError):
            ExtractiveSummarizer(method="invalid").summarize(self.text)

if __name__ == "__main__":
    unittest.main()
