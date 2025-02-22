# pysuma

### **🚀 PySummarizer - The Ultimate Text Summarization Library**

PySummarizer is a **powerful and intelligent** text summarization library designed for both **extractive** and **abstractive** summarization. It efficiently extracts key insights from PDFs and presents them in a structured, **bullet-point format**, making it perfect for academic research, content summarization, and AI-driven automation.

---

## **🌟 Features**
✅ **Supports Extractive & Abstractive Summarization**  
✅ **Seamlessly extracts text from PDFs & generates structured summaries**  
✅ **Utilizes TextRank, LSA, and LexRank for extractive summarization**  
✅ **Automatically adjusts bullet points based on text length**  
✅ **Customizable summary length to meet your needs**  
✅ **Command-line interface (CLI) for quick and efficient summarization**  
✅ **Easy-to-use and integrates effortlessly into Python projects**  

---

## **📌 Installation**
Get started in seconds! Install PySummarizer via **pip**:
```bash
pip install pysuma
```

---

## **🚀 Quick Start Guide**
Transform long PDFs into structured summaries in just a few lines of code.  

### **1️⃣ Import the Library**
```python
import pysuma as pyss
```

### **2️⃣ Define PDF Paths**
```python
pdf_path = "sample.pdf"      # Input PDF file
output_file = "summary.txt"  # Output summary file
```

### **3️⃣ Generate a Summarized Report**
```python
pyss.summarize_pdf(
    pdf_path,
    output_file,
    method="textrank",            # Choose from "textrank", "lsa", "lexrank"
    summary_type="extractive"      # Select either "extractive" or "abstractive"
)
```

### **4️⃣ Run & Retrieve Your Summary**
```bash
python script.py
```
✅ The summary will be saved in **summary.txt**, formatted as **bullet points**.

---

## **📄 Summary Output Example**
PySummarizer **automatically structures summaries into bullet points** for better readability:

```
• Learning enables acquiring new skills and knowledge.
• Supervised learning requires labeled datasets for training.
• Decision trees classify data using entropy and information gain.
• Reinforcement learning optimizes decision-making using rewards and penalties.
...
(Total bullet points depend on text length)
```

---

## **📊 Adaptive Bullet Point Summarization**
PySummarizer **dynamically adjusts the number of bullet points** based on text length:

| **Text Length (Characters)** | **Number of Bullet Points** |
|------------------------------|-----------------------------|
| 0 - 2500                     | 10                          |
| 2501 - 5000                  | 20                          |
| 5001 - 7500                  | 30                          |
| More than 7500               | 50                          |

🔹 **Ensures precise summarization without losing key details.**  

---

## **💻 CLI Usage (Command Line)**
Use PySummarizer directly from the terminal for quick PDF summarization:
```bash
pysuma sample.pdf summary.txt --method textrank --summary_type extractive
```
✔️ Perfect for automation & large-scale text processing.

---

## **📜 License**
PySummarizer is released under the **MIT License**, making it **open-source and free** for personal and commercial use.

---

🎯 **Transform lengthy PDFs into structured insights with PySummarizer today!**  
🔗 **Contribute or explore more:** [GitHub Repository](https://github.com/fardeenKhadri/pysuma)
```

---
