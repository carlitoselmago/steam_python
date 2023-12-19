from transformers import pipeline

#Més info d'aquest model
#https://huggingface.co/blog/sentiment-analysis-python

# Inicialitza la pipeline d'anàlisi de sentiments
profanity = pipeline("text-classification", model="Rishi-19/Profanity_Check_CustomData")

# Text d'exemple
text = "Piece of crap game"

# Realitza l'anàlisi de sentiments
result = profanity(text)

# Imprimeix el resultat
print(result)
