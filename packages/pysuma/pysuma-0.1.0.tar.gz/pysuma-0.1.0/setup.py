from setuptools import setup, find_packages

# Ensure UTF-8 encoding when reading README.md
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="pysuma",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "nltk",
        "sumy",
        "transformers",
        "PyPDF2",
    ],
    entry_points={
        "console_scripts": [
            "pysuma=pysuma.cli:main",
        ],
    },
    author="Fardeen Khadri",
    author_email="fardeeinshakhadrii@gmail.com",
    description="A flexible text summarization library supporting extractive and abstractive methods.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/fardeenKhadri/pysuma",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)


