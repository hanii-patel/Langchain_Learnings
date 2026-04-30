# Langchain_Learnings

This is my LangChain learning repository! This project serves as a personal knowledge base and sandbox where I explore, experiment with, and implement various features of the LangChain framework and Large Language Models (LLMs).

## Repository Structure

### 📁 `Langchain_models`
This folder contains my learnings around integrating and utilizing different LLM providers and models.
- **LLMs:** Basic implementation and interaction with standard text-completion models.
- **ChatModels:** Working with advanced conversational models, including testing the HuggingFace API and experimenting with model routers.

### 📁 `Langchain_prompts`
This folder is dedicated to mastering how we interact with LLMs using prompts, structured outputs, and user interfaces.

- **Prompt Engineering:** Working with prompt templates and loading configurations dynamically (`template.json`, `prompt_ui.py`).
- **Conversational Bots:** Building interactive chat loops and robustly managing conversation histories using `SystemMessage`, `HumanMessage`, and `AIMessage` (`chatbot.py`, `messages.py`).
- **Structured Outputs:** Techniques for forcing the LLM to return strictly formatted, parseable data to prevent hallucinations and errors:
  - **TypedDict:** Using native Python dictionary types for lightweight schema definition (`typeddict_demo.py`, `with_structured_output_typeddict.py`).
  - **Pydantic Models:** Leveraging Pydantic classes for powerful type-hinting, nested structures, and robust data validation (`pydantic_demo.py`, `with_structured_output_pydantic.py`).
  - **JSON Schemas:** Supplying raw JSON schemas directly to the model for language-agnostic data extraction (`json_schema.json`, `with_structured_output_json.py`).

---
*Continuously learning and adding more as I explore the world of AI engineering!*
