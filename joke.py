from transformers import pipeline

classJoke = pipeline("text-generation", "Parcurcik/joke_ai")

classJoke("JOKE:Чапаев")