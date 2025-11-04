from magentic import chatprompt, AssistantMessage, SystemMessage, UserMessage
from pydantic import BaseModel

from dotenv import load_dotenv
load_dotenv()

class Quote(BaseModel):
    quote: str
    person: str

@chatprompt(
    SystemMessage("You are an avid reader of financial literature"),
    UserMessage("What is your favourite quote from Warren Buffet?"),
    AssistantMessage(
        Quote(
            quote="Price is what you pay; value is what you get.",
            person="Warren Buffet",
        )
    ),
    UserMessage("What is your favourite quote from {person}?"),
)
def get_finance_quote(person: str) -> Quote: ...

print(get_finance_quote("Charlie Munger"))