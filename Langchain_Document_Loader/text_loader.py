from langchain_community.document_loaders import TextLoader
from langchain_google_genai import GoogleGenerativeAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv

load_dotenv()

model = GoogleGenerativeAI(model="gemini-2.5-flash")

prompt = PromptTemplate(
    template="write a summary of following poem \n {poem}",
    input_variables=["poem"]
)

paser = StrOutputParser()

loader = TextLoader("cricket.txt", encoding="utf-8")

document = loader.load()

print(document)
print(document[0])

chain = prompt | model | paser
print(chain.invoke({"poem" : document[0].page_content}))