# Open Machine Learning (OLML)

A collection of tools and examples for working with AI models and Language Learning Models (LLMs) focused on health-related applications.

## Overview

This repository contains various examples and implementations of AI-powered applications with a focus on:

- Retrieval Augmented Generation (RAG) systems
- Medical question answering
- Women's health information processing
- Integration with various LLM providers (OpenAI, etc.)

## Key Components

### Notebooks

- **gen-qa-openai.ipynb**: Retrieval Enhanced Generative Question Answering with OpenAI to resolve hallucinations in LLMs
- **rag_pubmed.ipynb**: Medical Question Answering system using LangChain and Mistral 7B with PubMed data

### Python Scripts

- **test_langchain.py**: Demonstrates LangChain integration with PubMed for medical information retrieval
- **womens_health.py**: Uses AIConfig to process women's health-related information
- **script.py**: Main script for running AI-based operations using various LLM providers

### Configuration Files

- **health.aiconfig.yaml**: Configuration for AI models focused on health-related prompts and contexts
- **.env**: Environment configuration for API keys from different LLM providers

## Getting Started

### Prerequisites

- Python 3.8+
- API keys for LLM providers:
  - OpenAI
  - Google (optional)
  - Hugging Face (optional)

### Installation

1. Clone this repository:
```bash
git clone https://github.com/yourusername/OLML.git
cd OLML
```

2. Create and activate a virtual environment (recommended):
```bash
python -m venv venv
source venv/bin/activate  # On Windows, use: venv\Scripts\activate
```

3. Install the required dependencies:
```bash
pip install -r requirements.txt  # Note: You may need to create this file
```

4. Configure your API keys:
   - Rename `.env.example` to `.env` (if available)
   - Add your API keys to the `.env` file

### Usage

#### Running Notebooks

Open the Jupyter notebooks in your preferred environment:
```bash
jupyter notebook
```

Then navigate to either `gen-qa-openai.ipynb` or `rag_pubmed.ipynb`.

#### Using the Python Scripts

Run the test_langchain.py script:
```bash
python test_langchain.py
```

Run the women's health script:
```bash
python womens_health.py
```

## License

[Include license information here]

## Acknowledgments

- This project uses various AI and ML libraries including LangChain, OpenAI, and others
- Medical data sources include PubMed and women's health resources 