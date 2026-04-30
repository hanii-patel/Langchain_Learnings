#without Output Parsers

from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate

load_dotenv()

model = ChatGoogleGenerativeAI(model = "gemini-2.5-flash")

#1st Prompt : Detailed Report
template1 = PromptTemplate(
    template="write a detailed report on {topic}",
    input_variables = ["topic"]
)

#2nd Prompt : Summary
template2 = PromptTemplate(
    template="write a 5 line summary on the following text /n {text}",
    input_variables = ["text"]
)

prompt1 = template1.format(topic = "Black Holes")
result = model.invoke(prompt1)
print(result.content)

prompt2 = template2.format(text = result.content)
result1 = model.invoke(prompt2)
print(result1.content)
