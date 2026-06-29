# Model Card: Mood Machine

This model card is for the Mood Machine project, which includes **two** versions of a mood classifier[cite: 2]:

1. A **rule based model** implemented in `mood_analyzer.py`[cite: 2, 3]
2. A **machine learning model** implemented in `ml_experiments.py` using scikit learn[cite: 1, 2]

---

## 1. Model Overview

**Model type:**  
I compared both models[cite: 2]. The baseline is a rule-based expert system (`mood_analyzer.py`)[cite: 2, 3] and the secondary is a simple machine learning classifier (`ml_experiments.py`)[cite: 1, 2].

**Intended purpose:**  
The system is built to classify short social-media style text snippets into one of four mood categories: positive, negative, neutral, or mixed[cite: 2, 6].

**How it works (brief):**  
* **Rule-Based Model:** It normalizes text by lowercasing and scrubbing out target punctuation marks[cite: 3]. It then checks for matching tokens against standard lists, tracks a cumulative score counter, and utilizes a basic lookahead loop to flip sentiment values when negation terms appear[cite: 3].
* **ML Model:** This script transforms the raw text inputs into numeric token-frequency tables using a Bag-of-Words vectorization technique and fits a logistic regression model to map text arrays directly to human categories[cite: 1, 2].

---

## 2. Data

**Dataset description:**  
The training text source consists of 14 target sentences within `SAMPLE_POSTS` matched perfectly with 14 target classifications inside `TRUE_LABELS`[cite: 6]. It builds upon the initial 6 starter sentences by adding modern variations[cite: 6].

**Labeling process:**  
Labels were selected to map literal text to clear subjective goals[cite: 6]. Conflicting sentences with simultaneous strong positive and negative elements were designated as `mixed`[cite: 6]. 

**Important characteristics of your dataset:**  
* Employs contemporary colloquial internet expressions (e.g., `"no cap"`, `"lowkey"`, `"highkey"`, `"vibe"`)[cite: 6].
* Employs inline Unicode expressions and visual symbols (e.g., `💀`, `🥲`)[cite: 6].
* Includes distinct sarcastic configurations where literal meaning conflicts with negative situational updates[cite: 6].

**Possible issues with the dataset:**  
The underlying corpus is incredibly sparse (14 instances)[cite: 6]. Because of its restricted size, it doesn't represent real-world text variations, and evaluating purely on training data can mask issues like extreme model over-optimization[cite: 2].

---

## 3. How the Rule Based Model Works

**Your scoring rules:**  
* **Preprocessing Rules:** Clears out leading/trailing whitespace, forces lowercasing, and strips out core punctuation markings (`.,!?;:()"'`)[cite: 3].
* **Scoring Assignment:** Positive array terms apply a `+1` increment, while negative array entries apply a `-1` decrement[cite: 3].
* **Negation Mechanics:** If a target negation token (`"not"`, `"never"`, `"no"`, `"dont"`, `"cant"`) is caught, a lookahead block skips standard processing and flips the polarity score of the subsequent mood token[cite: 3].
* **Threshold Architecture:** Simple logical bounds handle final designations: `score > 0` returns `"positive"`, `score < 0` returns `"negative"`, and a perfect zero balance `score == 0` drops back to `"neutral"`[cite: 3].

**Strengths of this approach:**  
It is completely transparent, deterministic, and doesn't require any expensive execution steps[cite: 3]. It is excellent at catching clean semantic inversion rules (e.g., converting `"not happy"` to a negative category)[cite: 3].

**Weaknesses of this approach:**  
It treats language linearly, which creates a critical vulnerability to score cancellation[cite: 3]. When a text piece simultaneously features multiple strong emotional expressions, the tokens cancel each other out, resulting in an inaccurate `"neutral"` label instead of mapping to `"mixed"`[cite: 3].

---

## 4. How the ML Model Works

**Features used:**  
Text strings are extracted into simple bag-of-words token frequency vectors via scikit-learn's `CountVectorizer` tool[cite: 1, 2].

**Training data:**  
The statistical setup maps inputs directly onto the active parallel arrays of `SAMPLE_POSTS` and `TRUE_LABELS` found within `dataset.py`[cite: 1, 2].

**Training behavior:**  
When executing the script over the updated dataset arrays, the algorithmic backend maps the distribution patterns quickly, achieving an absolute accuracy value of 1.00 directly across the evaluation dataset[cite: 1].

**Strengths and weaknesses:**  
* **Strengths:** It handles multi-word context variations implicitly without needing manual engineering rules or nested conditional statements[cite: 2]. It successfully resolved complex sarcastic sentences by learning the contextual combinations of terms like `"fantastic"` and `"delayed"`[cite: 1, 6].
* **Weaknesses:** It overfits aggressively to the training entries[cite: 2]. With a corpus of only 14 elements, it memorized specific sentences rather than developing broad language understanding[cite: 2, 6].

---

## 5. Evaluation

**How you evaluated the model:**  
Both modeling instances were evaluated by comparing their predictions directly against the 14 annotated examples in `dataset.py`[cite: 1, 2, 7]:
* The **Rule-Based model** scored a baseline accuracy of **0.57**[cite: 7].
* The **Machine Learning model** scored a training accuracy of **1.00**[cite: 1].

**Examples of correct predictions:**  
* `"Just dropped my entire lunch on the sidewalk 🥲"` $\rightarrow$ Both versions accurately resolved to `negative`[cite: 1, 7]. The rule-based version successfully picked this up because the Unicode symbol `🥲` was manually appended to the negative vocabulary list[cite: 3, 6].
* `"That guitar solo was absolutely sick"` $\rightarrow$ Both versions successfully resolved to `positive` because the flexible slang word `"sick"` was repositioned into the positive target array to handle modern slang context.

**Examples of incorrect predictions:**  
* `"Oh fantastic, my flight got delayed for another four hours"` $\rightarrow$ The rule-based engine outputted `neutral` instead of `negative`[cite: 7]. The single positive token (`"fantastic"`) and negative token (`"delayed"`) added up to a total score of zero, missing the obvious sarcastic subtext[cite: 3]. The ML model successfully caught this by recognizing word pairings across the dataset[cite: 1].
* `"Lowkey stressed about the midterm but highkey proud of how much I studied"` $\rightarrow$ The rule-based model misclassified this as `neutral` because the opposing emotional points nullified each other, failing to capture a true `mixed` emotion[cite: 3, 7].

---

## 6. Limitations

* **Vocabulary Fragility:** The rule-based model is completely blind to any expressive slang or words omitted from its hardcoded list configuration[cite: 3].
* **Literalism in Sarcasm:** The rule-based setup fails at parsing sarcastic context, interpreting individual word points literally[cite: 2, 3].
* **Severe Overfitting:** The ML model's perfect score is artificial[cite: 2]. It is highly sensitive to the 14 training examples and will degrade significantly when introduced to outside data variants[cite: 2, 6].

---

## 7. Ethical Considerations

* **Misinterpreting Crisis Contexts:** If deployed to monitor live user messages, the rule-based model could easily misinterpret serious human distress framed with sarcasm or mixed phrasing, failing to flag it for rapid intervention[cite: 2, 3].
* **Linguistic Bias:** The dataset relies on a highly specific subset of English internet expressions and slang[cite: 2]. It will naturally misclassify sentiment when processing inputs from other demographic backgrounds, age groups, or regional communities[cite: 2].

---

## 8. Ideas for Improvement

* **Implement Non-Zero Cancellation Systems:** Decouple the simple tracking index into separate positive and negative tracking paths so that overlapping high sentiments flag a true `mixed` emotion[cite: 3].
* **Introduce Weighted Values:** Swap out the rigid step tracking (`+/-1`) for variable weights, allowing heavy words like `"terrible"` or `"crashed"` to carry more weight than lighter terms[cite: 3].
* **Incorporate Dense Context Vectors:** Transition the ML setup from simple word counts (`CountVectorizer`) to TF-IDF transformations or advanced embeddings to capture semantic relationships more reliably[cite: 2].