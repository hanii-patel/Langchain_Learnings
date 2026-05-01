from langchain_core.runnables import chain
from langchain_google_genai import GoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate

load_dotenv()

prompt1 = PromptTemplate(
    template = "Generate a detailed report for {topic}",
    input_variables=['topic']
)
prompt2 = PromptTemplate(
    template= "Summarize the following report in 5 bullet points: {report}",
    input_variables=['report']
)

model = GoogleGenerativeAI(model="gemini-2.5-flash")

parser = StrOutputParser()

chain = prompt1 | model | parser | prompt2 | model | parser

result = chain.invoke({"topic": "unemployement in India"})

print(result)