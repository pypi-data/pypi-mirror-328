 
import argparse
from pysummarizer.extractive import ExtractiveSummarizer

def main():
    parser = argparse.ArgumentParser(description="PySummarizer CLI - Extractive Summarization")
    parser.add_argument("text", type=str, help="Text to summarize")
    parser.add_argument("--method", type=str, default="textrank", choices=["textrank", "lsa", "lexrank"], help="Summarization method")
    parser.add_argument("--sentences", type=int, default=3, help="Number of sentences in the summary")

    args = parser.parse_args()

    summarizer = ExtractiveSummarizer(method=args.method)
    summary = summarizer.summarize(args.text, sentences_count=args.sentences)

    print("\nSummary:")
    print(summary)

if __name__ == "__main__":
    main()
