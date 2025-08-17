import os
from langchain.chat_models import ChatOpenAI
from langchain.prompts import PromptTemplate

api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    raise ValueError("⚠️ Please set your OPENAI_API_KEY environment variable.")

llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0.7)

template = """
You are a customer service assistant.
1. Analyze the sentiment of the following review (positive, negative, neutral).
2. Write a short, polite, context-aware reply.

Customer review: "{review}"
"""
prompt = PromptTemplate(template=template, input_variables=["review"])

def get_feedback_response(review: str):
    chain = prompt | llm
    result = chain.invoke({"review": review})
    return result.content

if __name__ == "__main__":
    user_review = input("Enter customer review: ")
    response = get_feedback_response(user_review)
    print("\n🤖 Auto-response:\n", response)