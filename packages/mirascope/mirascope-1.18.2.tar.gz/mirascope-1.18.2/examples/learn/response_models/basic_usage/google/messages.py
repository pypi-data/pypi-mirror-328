from typing import cast

from mirascope.core import Messages, google
from pydantic import BaseModel


class Book(BaseModel):
    """An extracted book."""

    title: str
    author: str


@google.call("gemini-1.5-flash", response_model=Book)
def extract_book(text: str) -> Messages.Type:
    return Messages.User(f"Extract {text}")


book = extract_book("The Name of the Wind by Patrick Rothfuss")
print(book)
# Output: title='The Name of the Wind' author='Patrick Rothfuss'

response = cast(google.GoogleCallResponse, book._response)  # pyright: ignore[reportAttributeAccessIssue]
print(response.model_dump())
# > {'metadata': {}, 'response': {'id': ...}, ...}
