# mood_analyzer.py
"""
Rule based mood analyzer for short text snippets.

This class starts with very simple logic:
  - Preprocess the text
  - Look for positive and negative words
  - Compute a numeric score
  - Convert that score into a mood label
"""

from typing import List, Dict, Tuple, Optional

from dataset import POSITIVE_WORDS, NEGATIVE_WORDS


class MoodAnalyzer:
    """
    A very simple, rule based mood classifier.
    """

    def __init__(
        self,
        positive_words: Optional[List[str]] = None,
        negative_words: Optional[List[str]] = None,
    ) -> None:
        # Use the default lists from dataset.py if none are provided.
        positive_words = positive_words if positive_words is not None else POSITIVE_WORDS
        negative_words = negative_words if negative_words is not None else NEGATIVE_WORDS

        # Store as sets for faster lookup.
        self.positive_words = set(w.lower() for w in positive_words)
        self.negative_words = set(w.lower() for w in negative_words)

    # ---------------------------------------------------------------------
    # Preprocessing
    # ---------------------------------------------------------------------

    def preprocess(self, text: str) -> List[str]:
            """
            Convert raw text into a list of clean, lowercase tokens,
            removing basic punctuation to protect word matching.
            """
            # Lowercase and clean flanking whitespace
            cleaned = text.strip().lower()
            
            # Remove common punctuation marks
            punctuation = ".,!?;:()\"'"
            for char in punctuation:
                cleaned = cleaned.replace(char, "")
                
            tokens = cleaned.split()
            return tokens

    # ---------------------------------------------------------------------
    # Scoring logic
    # ---------------------------------------------------------------------

    def score_text(self, text: str) -> int:
        """
        Compute a numeric mood score. Loops over tokens, applies points,
        and flips the score of the next word if a negation word is found.
        """
        tokens = self.preprocess(text)
        score = 0
        
        negation_words = {"not", "never", "no", "dont", "cant"}
        skip_next = False

        for i, token in enumerate(tokens):
            # If we already evaluated this word as part of a negation pair, skip it
            if skip_next:
                skip_next = False
                continue

            # Lookahead check for negation
            if token in negation_words and (i + 1) < len(tokens):
                next_token = tokens[i + 1]
                
                # Check if the next word is a mood word
                if next_token in self.positive_words:
                    score -= 1  # "not happy" becomes negative
                    skip_next = True
                    continue
                elif next_token in self.negative_words:
                    score += 1  # "not bad" becomes positive
                    skip_next = True
                    continue

            # Standard word matching rule
            if token in self.positive_words:
                score += 1
            elif token in self.negative_words:
                score -= 1

        return score

    # ---------------------------------------------------------------------
    # Label prediction
    # ---------------------------------------------------------------------

    def predict_label(self, text: str) -> str:
            """
            Turn the numeric score for a piece of text into a mood label.
            """
            score = self.score_text(text)
            
            if score > 0:
                return "positive"
            elif score < 0:
                return "negative"
            else:
                return "neutral"

    # ---------------------------------------------------------------------
    # Explanations (optional but recommended)
    # ---------------------------------------------------------------------

    def explain(self, text: str) -> str:
        """
        Return a short string explaining WHY the model chose its label.

        TODO:
          - Look at the tokens and identify which ones counted as positive
            and which ones counted as negative.
          - Show the final score.
          - Return a short human readable explanation.

        Example explanation (your exact wording can be different):
          'Score = 2 (positive words: ["love", "great"]; negative words: [])'

        The current implementation is a placeholder so the code runs even
        before you implement it.
        """
        tokens = self.preprocess(text)

        positive_hits: List[str] = []
        negative_hits: List[str] = []
        score = 0

        for token in tokens:
            if token in self.positive_words:
                positive_hits.append(token)
                score += 1
            if token in self.negative_words:
                negative_hits.append(token)
                score -= 1

        return (
            f"Score = {score} "
            f"(positive: {positive_hits or '[]'}, "
            f"negative: {negative_hits or '[]'})"
        )
