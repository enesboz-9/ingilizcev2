# 🇬🇧 English Master

A professional, all-levels English reference site built with **Streamlit**.

## Features
- 📚 **Vocabulary** — 300+ words organized by topic and CEFR level (A1–C2)
- 🔤 **Sentence Patterns** — Essential grammar structures with formulas and examples
- 🎨 **Adjectives, Verbs & Adverbs** — The most useful describing and action words
- 💬 **Daily Expressions** — Phrasal verbs, idioms, and conversational phrases

## Getting Started

### 1. Clone the repo
```bash
git clone https://github.com/YOUR_USERNAME/english-master.git
cd english-master
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Run locally
```bash
streamlit run app.py
```

## Deploy on Streamlit Cloud
1. Push this repo to GitHub
2. Go to [share.streamlit.io](https://share.streamlit.io)
3. Connect your GitHub repo
4. Set **Main file path** to `app.py`
5. Click **Deploy** ✅

## Project Structure
```
english-master/
├── app.py              # Main Streamlit app
├── style.css           # Custom dark theme CSS
├── requirements.txt    # Python dependencies
└── data/
    ├── __init__.py
    ├── vocabulary.py   # Word lists by category & level
    ├── sentences.py    # Grammar patterns
    ├── adjectives.py   # Adjectives, verbs & adverbs
    └── phrases.py      # Phrasal verbs, idioms, daily expressions
```

## CEFR Level Color Guide
| Level | Color | Description |
|-------|-------|-------------|
| A1 | 🟢 Green | Beginner |
| A2 | 🔵 Teal | Elementary |
| B1 | 🔷 Blue | Intermediate |
| B2 | 🟣 Purple | Upper-Intermediate |
| C1 | 🔴 Red-Orange | Advanced |
| C2 | 🟡 Gold | Mastery |
