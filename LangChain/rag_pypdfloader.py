from langchain_community.document_loaders import PyPDFLoader, PyMuPDFLoader




#create an instance of the loader file that we shall be processing

file = PyMuPDFLoader(r"C:\Users\V I C T U S\OneDrive\Documents\e-books\zeena.pdf")


doc = file.load()

print(doc[0].page_content)