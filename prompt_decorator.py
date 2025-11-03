from magentic import prompt

from dotenv import load_dotenv
load_dotenv()

@prompt("Explain like I'm five this financial concept: {concept}")
def explain(concept: str) -> str: ...

print(explain("Subprime mortgage crisis"))