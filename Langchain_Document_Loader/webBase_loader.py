from langchain_community.document_loaders import WebBaseLoader
from langchain_google_genai import GoogleGenerativeAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv

load_dotenv()

model = GoogleGenerativeAI(model="gemini-2.5-flash")

prompt = PromptTemplate(
    template="Answer the following question \n {question} from the following text \n {text}",
    input_variables=["question", "text"]
)

paser = StrOutputParser()

url= "https://en.wikipedia.org/wiki/Deep_learning"
loader = WebBaseLoader(url)

docs = loader.load()

chain = prompt | model | paser

print(chain.invoke({"question" : "What is deep learning?", "text" : docs[0].page_content}))