from collections.abc import Iterable
from time import time
from pydantic import BaseModel
from magentic import prompt

from dotenv import load_dotenv
load_dotenv()

class Portfolio(BaseModel):
    equity_etf_pct: float
    bond_etf_pc: float
    crypto_etf_pc: float
    commodities_pc: float
    reasoning: str


@prompt("Create {n_portfolio} portfolios with varying deegress of risk apetite.")
def create_portfolios(n_portfolio: int) -> Iterable[Portfolio]: ...


start_time = time()
for portfolio in create_portfolios(3):
    print(f"{time() - start_time:.2f}s : {portfolio.model_dump_json(indent=2)}")