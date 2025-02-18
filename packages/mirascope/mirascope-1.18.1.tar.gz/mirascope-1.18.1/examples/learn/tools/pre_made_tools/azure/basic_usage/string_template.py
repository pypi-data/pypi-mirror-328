from mirascope.core import azure, prompt_template
from mirascope.tools import DuckDuckGoSearch


@azure.call("gpt-4o-mini", tools=[DuckDuckGoSearch])
@prompt_template("Recommend a {genre} book and summarize the story")
def research(genre: str): ...


response = research("fantasy")
if tool := response.tool:
    print(tool.call())
