from langchain_community.document_loaders import DirectoryLoader, PyPDFLoader

loader = DirectoryLoader(
    path='C:\Users\Acer\Desktop\LLMS\9.DocumentLoader\Building Machine Learning Systems with Python - Second Edition.pdf',
    glob='*.pdf',
    loader_cls=PyPDFLoader
)

docs = loader.lazy_load()

for document in docs:
    print(document.metadata)