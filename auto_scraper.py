from scrapegraphai.graphs import SmartScraperGraph
from dotenv import load_dotenv
import os

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

graph_config = {
    "llm": {
        "api_key": OPENAI_API_KEY,
        "model": "gpt-4-turbo-2024-04-09",
    },
}

smart_scraper_graph = SmartScraperGraph(
    prompt="List me all the news with their description.",
    # also accepts a string with the already downloaded HTML code
    source="https://www.wired.com/category/science/",
    config=graph_config
)

result = smart_scraper_graph.run()
print(result)


import json

output = json.dumps(result, indent=2)

line_list = output.split("\n")  

for line in line_list:
    print(line)