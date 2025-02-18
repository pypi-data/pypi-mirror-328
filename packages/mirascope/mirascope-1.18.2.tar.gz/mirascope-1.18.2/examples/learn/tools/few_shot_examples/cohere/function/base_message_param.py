from typing import Annotated

from pydantic import Field

from mirascope.core import BaseMessageParam, cohere


def get_book_author(
    title: Annotated[
        str,
        Field(
            ...,
            description="The title of the book.",
            examples=["The Name of the Wind"],
        ),
    ],
) -> str:
    """Returns the author of the book with the given title

    Example:
        {"title": "The Name of the Wind"}

    Args:
        title: The title of the book.
    """
    if title == "The Name of the Wind":
        return "Patrick Rothfuss"
    elif title == "Mistborn: The Final Empire":
        return "Brandon Sanderson"
    else:
        return "Unknown"


@cohere.call("command-r-plus", tools=[get_book_author])
def identify_author(book: str) -> list[BaseMessageParam]:
    return [BaseMessageParam(role="user", content=f"Who wrote {book}?")]


response = identify_author("The Name of the Wind")
if tool := response.tool:
    print(tool.call())
else:
    print(response.content)
