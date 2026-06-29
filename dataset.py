"""
Shared data for the Mood Machine lab.

This file defines:
  - POSITIVE_WORDS: starter list of positive words
  - NEGATIVE_WORDS: starter list of negative words
  - SAMPLE_POSTS: short example posts for evaluation and training
  - TRUE_LABELS: human labels for each post in SAMPLE_POSTS
"""

# ---------------------------------------------------------------------
# Starter word lists
# ---------------------------------------------------------------------

POSITIVE_WORDS = [
    "happy",
    "great",
    "good",
    "love",
    "excited",
    "awesome",
    "fun",
    "chill",
    "relaxed",
    "amazing",
    "bop", 
    "proud", 
    "vibe", 
    "fantastic",
    "sick", 
    "fire"
]

NEGATIVE_WORDS = [
    "sad",
    "bad",
    "terrible",
    "awful",
    "angry",
    "upset",
    "tired",
    "stressed",
    "hate",
    "boring",
    "delayed", 
    "dropped", 
    "🥲", 
    "💀",
    "crashed", 
    "failed", 
    "broke"
]

# ---------------------------------------------------------------------
# Starter labeled dataset
# ---------------------------------------------------------------------

# Short example posts written as if they were social media updates or messages.
SAMPLE_POSTS = [
    "I love this class so much",
    "Today was a terrible day",
    "Feeling tired but kind of hopeful",
    "This is fine",
    "So excited for the weekend",
    "I am not happy about this",
]

# Human labels for each post above.
# Allowed labels in the starter:
#   - "positive"
#   - "negative"
#   - "neutral"
#   - "mixed"
TRUE_LABELS = [
    "positive",  # "I love this class so much"
    "negative",  # "Today was a terrible day"
    "mixed",     # "Feeling tired but kind of hopeful"
    "neutral",   # "This is fine"
    "positive",  # "So excited for the weekend"
    "negative",  # "I am not happy about this"
]

# TODO: Add 5-10 more posts and labels.
#
# Requirements:
#   - For every new post you add to SAMPLE_POSTS, you must add one
#     matching label to TRUE_LABELS.
#   - SAMPLE_POSTS and TRUE_LABELS must always have the same length.
#   - Include a variety of language styles, such as:
#       * Slang ("lowkey", "highkey", "no cap")
#       * Emojis (":)", ":(", "🥲", "😂", "💀")
#       * Sarcasm ("I absolutely love getting stuck in traffic")
#       * Ambiguous or mixed feelings
#
# Tips:
#   - Try to create some examples that are hard to label even for you.
#   - Make a note of any examples that you and a friend might disagree on.
#     Those "edge cases" are interesting to inspect for both the rule based
#     and ML models.
#
# Example of how you might extend the lists:
#
# SAMPLE_POSTS.append("Lowkey stressed but kind of proud of myself")
# TRUE_LABELS.append("mixed")
#
# Remember to keep them aligned:
#   len(SAMPLE_POSTS) == len(TRUE_LABELS)

SAMPLE_POSTS.append("No cap this new album is an absolute bop 💀")
TRUE_LABELS.append("positive")

# 2. Slang + Mixed Feelings
SAMPLE_POSTS.append("Lowkey stressed about the midterm but highkey proud of how much I studied")
TRUE_LABELS.append("mixed")

# 3. Pure Sarcasm (Text implies positive, true intent is negative)
SAMPLE_POSTS.append("Oh fantastic, my flight got delayed for another four hours")
TRUE_LABELS.append("negative")

# 4. Melancholic/Gen-Z Humor Emoji
SAMPLE_POSTS.append("Just dropped my entire lunch on the sidewalk 🥲")
TRUE_LABELS.append("negative")

# 5. Flat/Matter-of-Fact statement
SAMPLE_POSTS.append("The package arrived on Thursday afternoon.")
TRUE_LABELS.append("neutral")

# 6. Ambiguous/Subtle Sarcasm
SAMPLE_POSTS.append("Wow, what an incredibly useful meeting that could have been an email")
TRUE_LABELS.append("negative")

# 7. Relieved/Chill Tone
SAMPLE_POSTS.append("Finally finished that project, time to just vibe for the rest of the night")
TRUE_LABELS.append("positive")

# 8. Strongly conflicting sentiments
SAMPLE_POSTS.append("I hate how much I love this terrible reality TV show")
TRUE_LABELS.append("mixed")


assert len(SAMPLE_POSTS) == len(TRUE_LABELS), f"Mismatched data lengths! Posts: {len(SAMPLE_POSTS)}, Labels: {len(TRUE_LABELS)}"