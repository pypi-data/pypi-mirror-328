import os
import PyPDF2
from pysuma.extractive import ExtractiveSummarizer
from pysuma.abstractive import AbstractiveSummarizer

def summarize_pdf(pdf_path, output_file, method="textrank", summary_type="extractive", min_length=20, max_length=2500):
    """
    Reads a PDF file, summarizes its text, and saves the summary as bullet points.

    :param pdf_path: Path to the input PDF file.
    :param output_file: Path to save the summary.txt file.
    :param method: Summarization method for extractive summarization ("textrank", "lsa", "lexrank").
    :param summary_type: "extractive" or "abstractive".
    :param min_length: Minimum length of the abstractive summary.
    :param max_length: Maximum length of the summary (default: 2500 characters).
    """
    if not os.path.exists(pdf_path):
        raise FileNotFoundError(f"PDF file '{pdf_path}' not found!")

    # Extract text from the PDF
    with open(pdf_path, "rb") as file:
        reader = PyPDF2.PdfReader(file)
        text = "\n".join([page.extract_text() for page in reader.pages if page.extract_text()])

    if not text.strip():
        raise ValueError("No text found in the PDF file!")

    # Determine the number of bullet points based on text length
    text_length = len(text)
    if text_length <= 2500:
        num_points = 10
    elif text_length <= 5000:
        num_points = 20
    elif text_length <= 7500:
        num_points = 30
    else:
        num_points = 50

    # Summarization based on type
    if summary_type == "extractive":
        summarizer = ExtractiveSummarizer(method=method)
        summary = summarizer.summarize(text, sentences_count=num_points)  # Set bullet count dynamically
    elif summary_type == "abstractive":
        summarizer = AbstractiveSummarizer()
        summary = summarizer.summarize(text, min_length=min_length, max_length=max_length)
    else:
        raise ValueError("Invalid summary type! Use 'extractive' or 'abstractive'.")

    # Trim the summary if it exceeds max_length
    summary = summary[:max_length]

    # Convert summary to bullet points
    summary_sentences = summary.split(". ")  # Split into sentences
    bullet_point_summary = "\n".join([f"• {sentence.strip()}" for sentence in summary_sentences[:num_points] if sentence.strip()])  # Format as bullet points

    # Ensure the output directory exists
    os.makedirs(os.path.dirname(os.path.abspath(output_file)), exist_ok=True)

    # Save bullet point summary to file
    with open(output_file, "w", encoding="utf-8") as out_file:
        out_file.write(bullet_point_summary)

    print(f"Summary saved to {output_file} ({num_points} bullet points, Max Length: {max_length} chars)")
