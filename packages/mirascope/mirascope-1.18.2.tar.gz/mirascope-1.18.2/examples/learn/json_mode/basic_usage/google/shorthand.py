import json

from mirascope.core import google


@google.call("gemini-1.5-flash", json_mode=True)
def get_book_info(book_title: str) -> str:
    return f"Provide the author and genre of {book_title}"


response = get_book_info("The Name of the Wind")
print(json.loads(response.content))
# Output: {'author': 'Patrick Rothfuss', 'genre': 'Fantasy'}
