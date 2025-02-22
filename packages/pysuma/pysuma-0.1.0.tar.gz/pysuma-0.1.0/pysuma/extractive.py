import nltk
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.text_rank import TextRankSummarizer
from sumy.summarizers.lsa import LsaSummarizer
from sumy.summarizers.lex_rank import LexRankSummarizer

nltk.download("punkt")

class ExtractiveSummarizer:
    """
    Extractive Summarizer supporting TextRank, LSA, and LexRank.
    """

    def __init__(self, method="textrank"):
        """
        Initialize summarizer with a method.

        :param method: "textrank", "lsa", or "lexrank"
        """
        self.method = method.lower()
        self.summarizers = {
            "textrank": TextRankSummarizer(),
            "lsa": LsaSummarizer(),
            "lexrank": LexRankSummarizer()
        }

    def summarize(self, text, sentences_count=3):
        """
        Summarize text using the selected method.

        :param text: Input text to summarize
        :param sentences_count: Number of sentences in the summary
        :return: Summarized text as a string
        """
        if self.method not in self.summarizers:
            raise ValueError(f"Unsupported summarization method: {self.method}")

        parser = PlaintextParser.from_string(text, Tokenizer("english"))
        summarizer = self.summarizers[self.method]

        summary = summarizer(parser.document, sentences_count)
        return " ".join([str(sentence) for sentence in summary])
