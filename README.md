# Persona-Based LinkedIn Writing Agent

A DSPy-optimized persona engine that generates LinkedIn posts in **Aman Gupta's** (Co-Founder & CMO, boAt Lifestyle) specific tone and style.

## 🎯 What This Does

This is **not** a general-purpose LinkedIn post generator. It's a **person-specific** AI agent trained to write like one person: Aman Gupta.

**Input:** Simple bullet points about what to write  
**Output:** A LinkedIn post that sounds authentically like Aman Gupta

---

## 🚀 Quick Start

### 1. Install Dependencies
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### 2. Add Your Gemini API Key
Create a `.env` file:
```bash
GEMINI_API_KEY=your_api_key_here
MODEL_NAME=gemini/gemini-2.5-flash
```


### 3. Run the Agent
```bash
python main.py
```

---

## 💡 How It Works

### The DSPy Optimization Process

Unlike traditional prompt engineering, this uses **DSPy optimization**:

1. **Training Data:** 6 carefully curated LinkedIn posts from Aman Gupta
   - Diverse tones: Reflective, Celebratory, Professional, Vulnerable, Strategic
   - Varied lengths: Short, Medium, Long
   - Different themes: Leadership, Failure, Manufacturing, Mentorship

2. **Optimizer:** `BootstrapFewShotWithRandomSearch`
   - Tests 6 different combinations of few-shot examples
   - Evaluates each using a custom Aman-specific style metric
   - Selects the best performing combination

3. **Evaluation Metric:** Checks for Aman's signature traits:
   - First-person narrative
   - Mix of Hindi-English phrases
   - Authentic voice markers ("we admit", "no suits", "failure teaches")
   - Emojis (🔥💪🙏🇮🇳)
   - Tone flexibility (can be professional OR casual)

4. **Result:** An optimized model that consistently generates posts in Aman's voice

---

## 📊 Training Data Quality

### Why Data Quality Matters

> "Garbage in, garbage out" - Your optimizer is only as good as your training data.

### Our Curation Approach

**Before:** Generic collection of 6 posts  
**After:** Scientifically balanced dataset

| Metric | Value | Status |
|--------|-------|--------|
| Tone Diversity | 6/6 unique tones | ✅ EXCELLENT |
| Length Variation | 1 short, 3 medium, 2 long | ✅ BALANCED |
| Hindi-English Mix | 4/6 posts | ✅ CONSISTENT |
| Topic Coverage | 6 different themes | ✅ DIVERSE |

**Tones Covered:**
1. 🟦 Reflective-Inspirational (Modi leadership story)
2. 🟩 Celebratory-Casual (Entrepreneur networking)
3. 🟧 Professional-Factual (Make in India)
4. 🟩 Reflective-Practical (Mentorship philosophy)
5. 🟦 Vulnerable-Inspirational (Failure teaches)
6. 🟧 Professional-Strategic (Global stage)

This diversity ensures the optimizer learns to handle **any** topic in Aman's voice.

---

## 🎮 Usage Examples

### Example 1: Celebratory Post
**Input:**
```
Indian women's cricket team won the world cup
```

**Output:**
```
Kya kamaal kar diya! 🔥🔥🔥

Our girls have done it! The Indian Women's Cricket Team are WORLD CHAMPIONS! 🏆🇮🇳

Pure desh ko garv hai! This isn't just a win; it's a statement...
```
---

## 🏗️ Architecture

```
PersonaTask/
├── main.py                 # Entry point, interactive CLI
├── src/
│   ├── config.py          # Configuration (persona details, API keys)
│   ├── data_preparation.py # Load & convert training data to DSPy format
│   ├── persona_model.py   # DSPy Signature & Module definition
│   ├── evaluator.py       # Aman-specific style metric
│   ├── optimizer.py       # DSPy BootstrapFewShotWithRandomSearch
│   └── generator.py       # Post generation & memory management
├── data/
│   ├── training.json      # 6 curated training posts
│   └── memory.json        # Saved generated posts
└── requirements.txt
```

---


## 📝 CLI Commands

| Command | Description |
|---------|-------------|
| `<content bullets>` | Generate a post about the given topic |
| `memory` | View last 5 saved posts |
| `quit` | Exit the application |

After generation, you'll be asked to save to memory (y/n).

---

## 🎯 Person-Specific Design

This is **intentionally** not generalizable:

1. **Hardcoded Persona:**
   ```python
   PERSON_NAME = "Aman Gupta"  # Not parameterized
   ```

2. **Aman-Specific Signature:**
   ```python
   """Generate a LinkedIn post in Aman Gupta's specific style"""
   ```

3. **Aman-Only Training Data:**
   - All 6 posts from Aman Gupta
   - No other personas

4. **Aman-Specific Evaluator:**
   - Checks for his signature phrases
   - Validates his tone patterns
   - Ensures his authentic voice

**Why?** Per requirements: *"The optimizer should not be general, it's specific to one person."*

---

## 🧪 Optimization Results

```
Training set size: 6 posts
Max demos per run: 2
Candidate programs to try: 6

Scores: [100.0, 0.0, 33.33, 50.0, 83.33, 100.0, 0.0, 100.0, 0.0]
Best score: 100.0%
```

The optimizer tested 9 candidate programs and selected the best one (100% style match).

---

## 📚 Key Learnings

### 1. Personas ≠ Static Prompts
Personas are **learned systems**, not hardcoded instructions. DSPy optimizes the prompt structure automatically.

### 2. Data Quality > Data Quantity
6 well-curated posts > 20 random posts. We balanced:
- Tone diversity (6 unique tones)
- Length variation (short/medium/long)
- Topic coverage (leadership, failure, manufacturing, etc.)

### 3. Person-Specific Metrics Matter
Generic "good writing" metrics don't work. We need Aman-specific checks:
- Does it sound like him?
- Does it use his phrases?
- Does it match his tone range?

### 4. Optimization Takes Time
With Gemini's free tier (10 req/min), optimization took ~7 minutes. Worth it for consistent quality.

---

## 🔧 Technical Stack

- **Framework:** DSPy (Stanford NLP)
- **LLM:** Google Gemini 2.5 Flash
- **Language:** Python 3.13
- **Optimizer:** BootstrapFewShotWithRandomSearch
- **Evaluation:** Custom boolean metric (3/5 criteria)

---

## 📖 References

- [DSPy Documentation](https://dspy.ai/)
- [DSPy Optimizers Guide](https://dspy.ai/learn/optimization/optimizers/)

