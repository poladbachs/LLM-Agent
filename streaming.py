from magentic import StreamedStr, prompt
import sys
import time

from dotenv import load_dotenv
load_dotenv()


@prompt("Explain to me {term} in a way a 5-year-old would understand.")
def describe_finance_term(term: str) -> StreamedStr: ...


print("\nStreaming response in real time...\n")
for chunk in describe_finance_term("liquidity"):
    sys.stdout.write(chunk)
    sys.stdout.flush()
    time.sleep(0.03)

print("\nDone!")