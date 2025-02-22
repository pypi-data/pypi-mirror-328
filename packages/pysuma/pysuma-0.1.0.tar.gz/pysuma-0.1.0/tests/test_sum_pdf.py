import sys
import os
import unittest
from reportlab.pdfgen import canvas

# Ensure the package can be found
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import pysuma as pyss  # Import the library correctly

class TestPDFSummarization(unittest.TestCase):
    def setUp(self):
        """Create a valid test PDF file in F:\pysuma\tests"""
        self.test_pdf = os.path.abspath("F:/pysuma/tests/test.pdf")
        self.output_file = os.path.abspath("F:/pysuma/tests/summary.txt")

        # Ensure the directory exists
        os.makedirs(os.path.dirname(self.test_pdf), exist_ok=True)

        # Generate a proper PDF using reportlab
        c = canvas.Canvas(self.test_pdf)
        c.drawString(100, 750, "Python is a powerful programming language.") 
        c.drawString(100, 730, "It is widely used in various domains.") 
        c.drawString(100, 710, "This is a test document for summarization.") 
        c.save()

    def test_summarize_pdf(self):
        """Test summarization from a PDF file"""
        try:
            # Summarize the PDF and save output in tests/summary.txt
            pyss.summarize_pdf(self.test_pdf, self.output_file, method="textrank", summary_type="extractive")

            # Debugging: Print the expected output file path
            print(f"DEBUG: Summary should be saved at {self.output_file}")

           
            self.assertTrue(os.path.exists(self.output_file), f"Expected summary file not found: {self.output_file}")

           
            with open(self.output_file, "r", encoding="utf-8") as f:
                summary = f.read()
                self.assertGreater(len(summary), 0, "Summary file is empty!")

        except Exception as e:
            self.fail(f"summarize_pdf() raised an exception: {e}")

    def tearDown(self):
        """Clean up test files"""
        if os.path.exists(self.test_pdf):
            os.remove(self.test_pdf)
        if os.path.exists(self.output_file):
            os.remove(self.output_file)

if __name__ == "__main__":
    unittest.main()
