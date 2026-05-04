from langchain_google_genai import GoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnableSequence , RunnableParallel , RunnablePassthrough

load_dotenv()

prompt1 = PromptTemplate(
    template="write a joke about {topic}",
    input_variables=["topic"]
)

model = GoogleGenerativeAI(model = "gemini-2.5-flash")
parser = StrOutputParser()

prompt2 = PromptTemplate(
    template="explain the following joke \n {joke}",
    input_variables=["joke"]
)

joke_gen_chain = RunnableSequence(
    prompt1 ,
    model ,
    parser
)

parallel_chain = RunnableParallel({
    "joke" : RunnablePassthrough(),
    "Explaination" : RunnableSequence(prompt2 , model , parser)
})

final_chain = RunnableSequence (joke_gen_chain , parallel_chain)

result = final_chain.invoke({"topic": "cricket"})

print(result)