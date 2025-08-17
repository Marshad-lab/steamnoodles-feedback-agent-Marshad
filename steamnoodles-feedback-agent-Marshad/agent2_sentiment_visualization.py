# agent2_sentiment_visualization.py
import os
import pandas as pd
import matplotlib.pyplot as plt
from langchain.chat_models import ChatOpenAI
from langchain.prompts import PromptTemplate

# Load OpenAI API key
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    raise ValueError("⚠️ Please set your OPENAI_API_KEY environment variable.")

# Initialize LLM
llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0)

# Prompt for classification
template = """
Classify the sentiment of the review as Positive, Negative, or Neutral.
Review: "{review}"
Answer with only one word: Positive, Negative, or Neutral.
"""
prompt = PromptTemplate(template=template, input_variables=["review"])

def classify_sentiment(review: str) -> str:
    chain = prompt | llm
    result = chain.invoke({"review": review})
    return result.content.strip()

def sentiment_trend(start_date: str, end_date: str, dataset_path="data/restaurant_reviews_sample.csv"):
    # Load dataset
    df = pd.read_csv(dataset_path)
    df["Date"] = pd.to_datetime(df["Date"])

    # Filter by date range
    mask = (df["Date"] >= start_date) & (df["Date"] <= end_date)
    df = df.loc[mask]

    # Classify each review
    df["Sentiment"] = df["Review"].apply(classify_sentiment)

    # Aggregate counts per day
    daily_counts = df.groupby([df["Date"].dt.date, "Sentiment"]).size().unstack(fill_value=0)

    # Plot
    daily_counts.plot(kind="bar", figsize=(10,5))
    plt.title(f"Sentiment Trend from {start_date} to {end_date}")
    plt.xlabel("Date")
    plt.ylabel("Number of Reviews")
    plt.xticks(rotation=45)
    plt.tight_layout()

    # Save chart
    output_path = "outputs/sentiment_plot.png"
    plt.savefig(output_path)
    print(f"📊 Sentiment trend chart saved to {output_path}")

if __name__ == "__main__":
    start = input("Enter start date (YYYY-MM-DD): ")
    end = input("Enter end date (YYYY-MM-DD): ")
    sentiment_trend(start, end)
