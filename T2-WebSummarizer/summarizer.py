# summarize any website contents by just passing url
# as llama3.2 model doesnt have capability of browsing this is not working as expected ,but works perfectly when change to openai api key

import sys
from pathlib import Path

# Add parent directory to path for imports
sys.path.insert(0, str(Path(__file__).parent.parent))

from openai import OpenAI
from Helpers.scraper import fetch_website_contents

openai = OpenAI(base_url="http://localhost:11434/v1", api_key="ollama")


def website_summarizer(url):

    system_prompt = """
        You are a highly skilled summarization assistant.
        Your job is to read the webpage content provided to you and produce
        a clear, structured, accurate, and non-biased summary.

        RULES:
        - Only summarize actual webpage text.
        - Ignore ads, navigation menus, sidebars, popups.
        - No hallucinations.
        - Keep the summary clean, simple, and structured.
    """

    user_prompt = f"""
        Summarize the contents of this webpage:

        URL: {url}

        Extract the text, clean it, and summarize it in the following format:

        1. Title of the Page
        2. 3–5 sentence summary
        3. Key bullet points
        4. Optional insights
    """

    response = openai.chat.completions.create(
        model="llama3.2",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt},
        ],
    )

    print(response.choices[0].message.content)

website_summarizer("https://docs.astral.sh/uv/getting-started/features/")
