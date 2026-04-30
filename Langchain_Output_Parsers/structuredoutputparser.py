from langchain_core.output_parsers import format_instructions
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser
from langchain_classic.output_parsers import StructuredOutputParser, ResponseSchema

load_dotenv()

model = ChatGoogleGenerativeAI(model = "gemini-2.5-flash")

schema = [
    ResponseSchema( name = 'Fact-1' , description = 'Fact 1 about the topic'),
    ResponseSchema( name = 'Fact-2' , description = 'Fact 2 about the topic'),
    ResponseSchema( name = 'Fact-3' , description = 'Fact 3 about the topic'),
]


parser = StructuredOutputParser.from_response_schemas(schema)

template = PromptTemplate(
    template='Give 3 facts about the {topic} \n {format_instructions}',
    input_variables=['topic'],
    partial_variables={
        'format_instructions': parser.get_format_instructions()
    }
)

prompt = template.format(topic = "Black Holes")
result = model.invoke(prompt)
final_result = parser.parse(result.content)
print(final_result)
