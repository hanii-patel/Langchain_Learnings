from langchain_community.document_loaders import PyPDFLoader

loader = PyPDFLoader("dl-curriculum.pdf")

documents = loader.load()

# print(documents)
print(documents[0])

# print(len(documents))