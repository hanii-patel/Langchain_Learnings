from langchain_google_genai import GoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnableSequence , RunnableParallel

load_dotenv()

model = GoogleGenerativeAI(model = "gemini-2.5-flash")
parser = StrOutputParser()

prompt1 = PromptTemplate(
    template = "Generate a tweet about {topic}",
    input_variables = ["topic"]
)

prompt2 = PromptTemplate(
    template="generate a linkedIn post about {topic}",
    input_variables = ["topic"]
)

parser = StrOutputParser()

parallel_chain = RunnableParallel({
    "tweet" : prompt1 | model | parser,
    "linkedIn" : prompt2 | model | parser
})

result = parallel_chain.invoke({"topic": "AI"})
print(result)

# prompt3 = PromptTemplate(
#     template="merge the following tweet and linkedIn post into a single document \n {tweet} \n {linkedIn}",
#     input_variables = ["tweet", "linkedIn"]
# )