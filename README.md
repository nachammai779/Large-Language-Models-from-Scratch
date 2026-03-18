<div align="center">

# 🧠 Large Language Models from Scratch

**Demystifying the inner workings of LLMs — one building block at a time.**

![Python](https://img.shields.io/badge/Python-3.8+-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Jupyter](https://img.shields.io/badge/Jupyter-Notebook-F37626?style=for-the-badge&logo=jupyter&logoColor=white)
![NLP](https://img.shields.io/badge/NLP-Natural%20Language%20Processing-blueviolet?style=for-the-badge)

*A hands-on collection of notebooks that build core LLM components entirely from scratch — no black boxes, just pure understanding.*

---

</div>

## 🌟 Overview

Ever wondered what really happens inside a Large Language Model? This repository strips away the abstraction layers and rebuilds the foundational components of LLMs from the ground up. Each notebook is a self-contained deep dive into a critical piece of the LLM puzzle, written with clarity and rich explanations.

Whether you're a student, researcher, or engineer looking to solidify your understanding of how modern language models work under the hood, this repository is your hands-on companion.

---

## 📂 What's Inside

### 📘 Byte Pair Encoding from Scratch
> `Byte_Pair_Encoding_from_Scratch.ipynb`
>
> A complete implementation of the **BPE tokenization algorithm** — the same subword tokenization strategy used by GPT and many modern LLMs. Learn how raw text is broken down into tokens that a model can understand, starting from individual characters and iteratively merging the most frequent pairs.
>
> ### 📊 BPE Compression Ratio Comparison
> > `BPE_Compression_Ratio_Comparison_Notebook.ipynb`
> >
> > How efficient is BPE really? This notebook benchmarks **compression ratios** across different vocabulary sizes and text corpora, giving you an intuitive feel for the tradeoffs between vocabulary size, token granularity, and compression efficiency.
> >
> > ### 🔧 Building an LLM Tokenizer, Encoder & Decoder from Scratch
> > > `Build_LLM_Scratch_tokenizer_encoder_decoder.ipynb`
> > >
> > > The full pipeline: from **raw text → tokens → encoded IDs → decoded text**. This notebook walks through building a complete tokenizer with encoder and decoder functions, mirroring the preprocessing steps that every LLM relies on before a single weight is trained.
> > >
> > > ### 🔮 Next Token Prediction Probability
> > > > `Next_Token_Prediction_Probability.ipynb`
> > > >
> > > > The heart of autoregressive language modeling — **predicting the next token**. This notebook implements the probability distributions and sampling strategies that allow a language model to generate coherent text, one token at a time.
> > > >
> > > > ### 🐳 Deployment Ready
> > > > > `Dockerfile` + `handler.py`
> > > > >
> > > > > Production-ready containerization with a Docker setup and handler script, demonstrating how to package and deploy LLM components as a service.
> > > > >
> > > > > ---
> > > > >
> > > > > ## 🎯 Key Learning Outcomes
> > > > >
> > > > > - **Tokenization Mastery** — Understand BPE at the algorithmic level, not just as an API call
> > > > > - - **Encoding & Decoding Pipelines** — Build the bridge between human-readable text and model-ready numerical representations
> > > > >   - - **Probability & Sampling** — Grasp how next-token prediction drives text generation
> > > > >     - - **Compression Analysis** — Evaluate tokenizer efficiency with real metrics
> > > > >       - - **Deployment Skills** — Package NLP components into deployable containers
> > > > >        
> > > > >         - ---
> > > > >
> > > > > ## 🚀 Getting Started
> > > > >
> > > > > ```bash
> > > > > # Clone the repository
> > > > > git clone https://github.com/nachammai779/Large-Language-Models-from-Scratch.git
> > > > >
> > > > > # Navigate into the project
> > > > > cd Large-Language-Models-from-Scratch
> > > > >
> > > > > # Launch Jupyter
> > > > > jupyter notebook
> > > > > ```
> > > > >
> > > > > ---
> > > > >
> > > > > ## 🛠️ Tech Stack
> > > > >
> > > > > | Technology | Purpose |
> > > > > |:---:|:---:|
> > > > > | 🐍 Python | Core language |
> > > > > | 📓 Jupyter Notebook | Interactive development |
> > > > > | 🐳 Docker | Containerization & deployment |
> > > > >
> > > > > ---
> > > > >
> > > > > ## 👩‍💻 Author
> > > > >
> > > > > **Nachammai Palaniappan**
> > > > > Data Engineer · Machine Learning Researcher · LLM Enthusiast
> > > > >
> > > > > [![GitHub](https://img.shields.io/badge/GitHub-nachammai779-181717?style=flat-square&logo=github)](https://github.com/nachammai779)
> > > > > [![LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-0A66C2?style=flat-square&logo=linkedin)](https://linkedin.com/in/nachammai-palaniappan-710094195)
> > > > >
> > > > > ---
> > > > >
> > > > > <div align="center">

*⭐ If this repository helped you understand LLMs better, consider giving it a star!*

</div>
