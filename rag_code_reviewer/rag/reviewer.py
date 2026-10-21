import os
from google import genai
from google.genai import types
from .retriever import format_context

MODEL = "gemini-3.8-flash"

SYSTEM_PROMPT = """You are an expert senior software engineer doing a code review.
You get the code and relevant team guidelines.

Write the review in Markdown with these sections:
## Summary
## Issues  (severity: Critical/High/Medium/Low, where, what, why)
## Suggested Fixes  (corrected code snippets)
## Guideline Check  (cite the guideline file name in brackets)
## Score  (1-10 with one-line reason)

Be specific and honest. Do not invent issues."""


def review_code(code, language, guidelines, api_key=None):
    client = genai.Client(api_key=api_key or os.getenv("GEMINI_API_KEY"))

    user_message = (
        f"Language: {language}\n\n"
        f"Relevant guidelines:\n{format_context(guidelines)}\n\n"
        f"Code to review:\n{code}"
    )

    response = client.models.generate_content(
        model=MODEL,
        contents=user_message,
        config=types.GenerateContentConfig(system_instruction=SYSTEM_PROMPT),
    )
    return response.text