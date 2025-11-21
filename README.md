# ML Email Classifier + Summarizer

## Overview

This project is an end-to-end machine learning system that:

1. Takes an email as input (subject + body text).
2. Predicts what type of email it is (e.g., spam vs ham, or categories like "work", "promo", "personal").
3. Generates a short summary of the email content.
4. Exposes this functionality through a simple web interface and a Flask API.

The goal is to practice:

- Basic Python programming
- Applied machine learning on text (NLP)
- Building and wiring a small real-world system

You’ll go from **raw text** → **cleaned text** → **numeric features** → **trained model** → **API + UI**.

---

## Core Features (Target)

- 🔤 **Text preprocessing**

  - Lowercasing, removing noise (URLs, special characters, etc.)
  - Tokenization (splitting text into words)
  - Optional stop-word removal

- 📊 **Feature extraction with TF-IDF**

  - Convert emails into numeric vectors using TF-IDF
  - Understand term frequency vs inverse document frequency intuitively

- 🧠 **Email classification model**

  - Train a simple baseline model:
    - Logistic Regression **or**
    - Naive Bayes
  - Evaluate accuracy on a small labeled dataset

- 📝 **Email summarization**

  - Start simple (rule-based / extractive summarization)
  - Optionally use NLTK tools or a transformer-based API to improve summaries

- 🌐 **Flask API**

  - Expose an endpoint like `/classify_and_summarize`
  - Input: JSON with email subject + body
  - Output: JSON with predicted label and generated summary

- 🖥️ **Simple UI**
  - Minimal web page where you can:
    - Paste an email
    - Click a button
    - See the predicted label + summary

---

## Tech Stack

- **Language:** Python 3
- **Libraries (planned):**
  - `scikit-learn` – TF-IDF, Logistic Regression / Naive Bayes
  - `nltk` – basic NLP utilities (tokenization, stopwords, etc.)
  - (optional) a transformer-based API client for better summarization
  - `flask` – backend API
- **Frontend:** very simple HTML/CSS/JS or a minimal template rendered by Flask

---

## Learning Objectives

By the end of this project you should be able to:

1. Write and structure basic Python scripts for a real project.
2. Explain what TF-IDF is and why it’s used for text.
3. Train and evaluate a simple text classifier.
4. Implement a basic summarization pipeline.
5. Build and run a small Flask API.
6. Connect a backend model to a simple UI.

---

## High-Level Roadmap (Approx. 2 Weeks)

**Phase 1 – Foundations & Playground (Days 1–3)**

- Set up project structure and environment.
- Load and clean sample emails.
- Play with basic text statistics and preprocessing.

**Phase 2 – TF-IDF + Classifier (Days 4–7)**

- Build a small labeled dataset of emails.
- Implement TF-IDF feature extraction.
- Train and evaluate Logistic Regression / Naive Bayes.

**Phase 3 – Summarization (Days 8–10)**

- Implement a basic extractive summarizer.
- Optionally plug in a transformer API for better summaries.

**Phase 4 – API + UI (Days 11–14)**

- Wrap the model in a Flask API.
- Build a minimal UI to interact with the system.
- Clean up code, write short documentation, and test.

---

## Status

- [ ] Project environment set up
- [ ] Basic text preprocessing script
- [ ] TF-IDF pipeline
- [ ] Classifier trained
- [ ] Summarizer implemented
- [ ] Flask API built
- [ ] Simple UI working
- [ ] Final cleanup and documentation

---
