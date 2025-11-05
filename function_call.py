import os
import requests
import json
from magentic import prompt, FunctionCall

from dotenv import load_dotenv
load_dotenv()

AV_API_KEY = os.getenv("AV_API_KEY")

def get_daily_price(ticker: str, api_key: str = AV_API_KEY) -> dict:
    url = f'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={ticker}&apikey={api_key}'
    r = requests.get(url)
    data = r.json()
    return data['Time Series (Daily)']

@prompt(
    "Use the appropriate search function to answer: {question}",
    functions=[get_daily_price],
)
def perform_search(question: str) -> FunctionCall[str]: ...

output = perform_search("What is the daily price data of AAPL?")
print(json.dumps(output(), indent=2))