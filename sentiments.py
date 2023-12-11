from transformers import pipeline

#Més info d'aquest model
#https://huggingface.co/blog/sentiment-analysis-python

# Inicialitza la pipeline d'anàlisi de sentiments
sentiment_analyzer = pipeline("sentiment-analysis")

# Text d'exemple
text = "I fucking love this shit!"

# Realitza l'anàlisi de sentiments
result = sentiment_analyzer(text)

# Imprimeix el resultat
print(result)
