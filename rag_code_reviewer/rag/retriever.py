def build_query(code, language):
    """Use the language and the start of the code as the search query."""
    return f"{language} code review best practices, bugs, security: {code.strip()[:1500]}"


def retrieve_guidelines(store, code, language, k=4):
    return store.query(build_query(code, language), k=k)


def format_context(results):
    """Turn the list of chunks into one text block for the prompt."""
    if not results:
        return "No project guidelines available."
    return "\n\n".join(f"[{r['source']}]\n{r['text']}" for r in results)
