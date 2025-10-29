from textblob import TextBlob # Performs sentiment polarity calculation  
import gradio as gr # Used to quickly create web-based user interfaces (UIs) for machine Learning models or Python functions. 
from openai import OpenAI # Used for: Accessing OpenAI's Language models (Like GPT-4), embeddings, etc., via API calls.

def analyze_sentiment(text):
    sentiment_score = TextBlob(text).sentiment.polarity
    if sentiment_score > 0 :
        sentiment = "Positive"
    elif sentiment_score < 0 :
        sentiment = "Negative"
    else:
        sentiment = "Neutral"
    return sentiment

iface = gr. Interface(fn=analyze_sentiment
                      ,inputs="text"
                      ,outputs="text"
                      ,title="AI Sentiment Analyzer"
                      ,description="Enter a sentence, and the AI will analyze its sentiment!")
iface.launch()
