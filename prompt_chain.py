import csv
from magentic import prompt_chain
import os
import requests
import json

from dotenv import load_dotenv
load_dotenv()

AV_API_KEY = os.getenv("AV_API_KEY")

def get_earnings_calendar(ticker: str, api_key: str = AV_API_KEY) -> list:
    url = f"https://www.alphavantage.co/query?function=EARNINGS_CALENDAR&symbol={ticker}&horizon=12month&apikey={api_key}"
    with requests.Session() as s:
        download = s.get(url)
        decoded_content = download.content.decode('utf-8')
        cr = csv.reader(decoded_content.splitlines(), delimiter=',')
        my_list = list(cr)
    return my_list


@prompt_chain(
    "What's {ticker} expected earnings dates for the next 12 months?",
    functions=[get_earnings_calendar],
)
def get_earnings(ticker: str) -> str: ...


print(get_earnings("IBM"))