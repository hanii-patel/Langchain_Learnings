from langchain_google_genai import GoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnableSequence

load_dotenv()

prompt = PromptTemplate(
    template="write a joke about {topic}",
    input_variables=["topic"]
)

model = GoogleGenerativeAI(model = "gemini-2.5-flash")
parser = StrOutputParser()

promot2 = PromptTemplate(
    template="explain the following joke \n {joke}",
    input_variables=["joke"]
)

chain = RunnableSequence(prompt , model , parser , promot2 , model , parser)

print(chain.invoke({"topic": "AI"}))

# chain.get_graph().print_ascii()
