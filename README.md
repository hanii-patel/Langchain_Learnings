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

### 📁 `Langchain_Output_Parsers`
This folder covers various methods to parse raw text outputs from the LLM into structured data formats.
- **String Parsers:** Extracting clean text using `StrOutputParser` (`stroutputparser.py`, `stroutputparser1.py`).
- **JSON Parsers:** Converting responses into JSON format using `JsonOutputParser` (`jsonoutputparser.py`).
- **Structured Output Parsers:** Defining explicit schemas with `ResponseSchema` and extracting strictly formatted data using `StructuredOutputParser` (`structuredoutputparser.py`).
- **Pydantic Parsers:** Using Pydantic models to automatically extract, validate, and type-hint outputs (`pydanticoutputparser.py`).

### 📁 `Langchain_Chains`
This folder explores LangChain Expression Language (LCEL) and how to compose multiple components together to build complex workflows.
- **Simple Chains:** Creating a basic end-to-end chain using the `|` pipe syntax (`simple_chain.py`).
- **Sequential Chains:** Linking multiple chains together where the output of one step feeds directly into the next (`sequential_chain.py`).
- **Parallel Chains:** Executing tasks concurrently using `RunnableParallel` and merging their outputs downstream (`parallel_chain.py`).
- **Conditional Chains (Routing):** Using `RunnableBranch` and custom `RunnableLambda` functions to dynamically route execution based on intermediate outputs like sentiment analysis (`conditional_chain.py`).

### 📁 `Langchain_Runnables`
This folder dives deeper into LangChain's core `Runnable` interface, allowing for highly customizable, declarative pipelines.
- **RunnableSequence:** Combining steps explicitly without using the pipe (`|`) operator (`runnable_sequence.py`).
- **RunnableParallel:** Running multiple distinct processes concurrently and combining their outputs into a single dictionary (`runnable_parallel.py`).
- **RunnablePassthrough:** Passing inputs unchanged to later stages while still evaluating side branches (`runnable_passthrough.py`).
- **RunnableLambda:** Converting custom Python functions into executable components within a chain (`runnable_lambda.py`).
- **RunnableBranch:** Dynamically routing data through different paths based on conditions or output sizes (`runnable_branch.py`).

### 📁 `Langchain_Document_Loader`
This folder covers how to ingest different types of data sources and convert them into LangChain `Document` objects for downstream processing.
- **Text Loader:** Loading basic `.txt` files and passing the content into a summarization chain (`text_loader.py`).
- **CSV Loader:** Ingesting structured data row-by-row from `.csv` files (`CSV_loader.py`).
- **PDF Loader:** Reading and parsing `.pdf` files using `PyPDFLoader` (`pdf_loader.py`).
- **Directory Loader:** Bulk loading multiple documents (e.g., all PDFs in a folder) using `DirectoryLoader` (`directory_loader.py`).
- **WebBase Loader:** Scraping and extracting clean text from web pages using BeautifulSoup (`webBase_loader.py`).

### 📁 `Langchain_Text_Splitters`
This folder demonstrates different techniques for splitting large text documents into smaller chunks for LLMs to process effectively.
- **Length-Based Splitting:** Breaking text into chunks purely based on character count (`length_based.py`).
- **Text Structure-Based Splitting:** Using `RecursiveCharacterTextSplitter` to intelligently split text based on paragraphs, sentences, and words (`text_structure_based.py`).
- **Python Code Splitting:** Splitting Python source code while respecting its syntax and logical blocks (`python_code_splitting.py`).
- **Markdown Splitting:** Splitting Markdown files while respecting headers, code blocks, and markdown syntax (`markdown_splitting.py`).
- **Semantic Meaning-Based Splitting:** Using `SemanticChunker` and embeddings to group text by contextual meaning rather than arbitrary length (`semantic_meaning_based.py`).

---
*Continuously learning and adding more as I explore the world of AI engineering!*
