# steamnoodles-feedback-agent-Marshad
# SteamNoodles Automated Restaurant Feedback Agents

## Project Description
This project automates the handling of customer feedback for the SteamNoodles restaurant chain using AI agents. One agent automatically responds to customer reviews by analyzing sentiment, while another generates sentiment trend visualizations over a user-selected date range.

## Technologies Used
- Python 3.12
- LangChain
- OpenAI GPT-3.5-turbo
- pandas
- matplotlib
- Virtual Environment (venv)

## Setup Instructions

1. Clone the repository:https://github.com/YourUsername/steamnoodles-feedback-agent-YourName.git
2. Navigate to the project folder:cd steamnoodles-feedback-agent-Marshad
3. Create and activate a virtual environment:
- Windows:
  ```
    python -m venv venv
  venv\Scripts\activate
  ```
4. Install dependencies:pip install -r requirements.txt
5. Set your OpenAI API key as an environment variable:
- On Windows (Command Prompt):
  ```
  setx OPENAI_API_KEY "your_api_key_here"
  ```
  Restart your terminal or IDE after this.
## Running the Agents

- To run the Customer Feedback Response Agent: python agent1_feedback_response.py

- To run the Sentiment Visualization Agent:python agent2_sentiment_visualization.py

You will be prompted to enter a start date and end date in `YYYY-MM-DD` format.

## Sample Output

- Auto-response example from Feedback Response Agent:
> "Thank you for your positive feedback! We appreciate your kind words."

- Sentiment trend plot saved as:outputs/sentiment_plot.png

## Project Structure

── agent1_feedback_response.py # Feedback response AI agent code
├── agent2_sentiment_visualization.py # Sentiment visualization AI agent code
├── data/
│ └── restaurant_reviews_sample.csv # Sample dataset of restaurant reviews
├── outputs/
│ └── sentiment_plot.png # Generated sentiment trend plot
├── requirements.txt # Python package dependencies
├── README.md # Project documentation (this file)
└── venv/ # Virtual environment folder


## Author

Your Name : Marshad M M M
Your University : University of Moratuwa
Year  : 2023





