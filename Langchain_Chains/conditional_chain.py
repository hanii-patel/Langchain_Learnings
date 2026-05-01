from langchain_google_genai import GoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser , PydanticOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnableParallel , RunnableBranch, RunnableLambda
from pydantic import BaseModel, Field
from typing import Literal

load_dotenv()

model = GoogleGenerativeAI(model="gemini-2.5-flash")
parser = StrOutputParser()

class Feedback(BaseModel):
    sentiment: Literal["positive", "negative"] = Field(description="Sentiment of the given text")

parser2 = PydanticOutputParser(pydantic_object=Feedback)
   
prompt1 = PromptTemplate(
    template="""
    Classify the following sentiment of the given text in positive or negative \n {feedback} \n {format_instructions}
    """,
    input_variables=["feedback"],
    partial_variables={
        "format_instructions": parser2.get_format_instructions()
    }
)

classifier_chain = prompt1 | model | parser2

prompt2 = PromptTemplate(
    template="""
     write an appropriate reply to this positive feedback \n {feedback}
    """,
    input_variables=["feedback"]
)


prompt3 = PromptTemplate(
    template="""
     write an appropriate reply to this negative feedback \n {feedback}
    """,
    input_variables=["feedback"]
)


branch_chain = RunnableBranch(
    (lambda x: x.sentiment == "positive", prompt2 | model | parser),
    (lambda x: x.sentiment == "negative", prompt3 | model | parser),
    RunnableLambda(lambda x: "couldn't find sentiment in feedback")
)

chain= classifier_chain | branch_chain

result = chain.invoke({"feedback": "i hate this product"})

print(result)