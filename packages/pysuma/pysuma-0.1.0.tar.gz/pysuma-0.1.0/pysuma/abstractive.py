 
from transformers import pipeline

class AbstractiveSummarizer:
    """
    Abstractive Summarizer using a pre-trained Transformer model.
    """

    def __init__(self, model_name="facebook/bart-large-cnn"):
        """
        Initialize the summarizer with a pre-trained model.

        :param model_name: Pre-trained model for summarization (default: "facebook/bart-large-cnn").
        """
        self.model_name = model_name
        self.summarizer = pipeline("summarization", model=self.model_name)

    def summarize(self, text, min_length=20, max_length=100):
        """
        Generate an abstractive summary.

        :param text: Input text to summarize
        :param min_length: Minimum length of the summary
        :param max_length: Maximum length of the summary
        :return: Summarized text as a string
        """
        if not text.strip():
            return ""
        
        

        summary = self.summarizer(text, min_length=min_length, max_length=max_length, do_sample=False)
        return summary[0]['summary_text']


#  █████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████