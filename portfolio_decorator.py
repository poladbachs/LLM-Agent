from magentic import prompt
from pydantic import BaseModel

from dotenv import load_dotenv
load_dotenv()

class Portfolio(BaseModel):
    equity_etf_pct: float
    bond_etf_pc: float
    crypto_etf_pc: float
    commodities_pc: float
    reasoning: str

@prompt("Create a strong portfolio of {size} allocation size.")
def create_portfolio(size: str) -> Portfolio: ...

portfolio = create_portfolio("$50,000")
print(portfolio.model_dump_json(indent=2))