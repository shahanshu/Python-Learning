from langchain.text_splitter import CharacterTextSplitter

from langchain_community.document_loaders import PyPDFLoader

pdf_path= r"C:\Users\V I C T U S\OneDrive\Desktop\python_learning\LangChain\docs\BRUCE.pdf"


text= "The human brain is one of the most complex and fascinating organs in the body. It acts as the control center, managing thoughts, emotions, memory, and movement. Composed of billions of neurons, the brain communicates through electrical signals, allowing humans to think, learn, and adapt. The cerebrum governs reasoning and decision-making, while the cerebellum coordinates balance and movement. The brainstem controls vital functions like breathing and heartbeat. Despite weighing only about three pounds, it consumes a large amount of the body’s energy. Scientists continue to study the brain to better understand conditions such as Alzheimer’s and strokes. Protecting brain health through proper nutrition, exercise, and rest is essential, as it is the foundation of human intelligence and consciousness."

loader= PyPDFLoader(pdf_path)

doc= loader.load()
splitter = CharacterTextSplitter(
    separator='',
    chunk_size=10,
    chunk_overlap=3,
)


result = splitter.split_documents(doc)
f1= result[0].metadata
f2=result[0].page_content

print(f1)

print('')

print(f2)
