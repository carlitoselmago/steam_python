#https://github.com/mshenoda/roberta-spam
from transformers import pipeline

# Initialize the spam detection pipeline
# Note: This model is primarily for emotion detection, but it can be a starting point
# for distinguishing between normal texts (e.g., joy, sadness) and unusual patterns (e.g., spam-like texts).
spam_detector = pipeline("text-classification", model="mshenoda/roberta-spam")

# Example text
text = "Hi"

# Perform spam detection
#LABEL_0 = ham
#LABEL_1 = spam
result = spam_detector(text)

# Print the result
print(result)
