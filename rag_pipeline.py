from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnableParallel, RunnablePassthrough, RunnableLambda
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
import os
from dotenv import load_dotenv
load_dotenv()


os.environ["LANGCHAIN_PROJECT"] = "SIM RAG chatbot"

PDF_PATH = "/home/tacktile/SIM_SupportBot/knowledge_base/SIM_Knowledge_Base_v3.pdf"

#1] Load PDF
loader = PyPDFLoader(PDF_PATH)
docs = loader.load()

#2] Split into chunks
text_splitter = RecursiveCharacterTextSplitter(chunk_size = 1000, chunk_overlap = 200)
splits = text_splitter.split_documents(docs)

#3] Create embeddings
embeddings = OpenAIEmbeddings(model = "text-embedding-3-small")
vs = FAISS.from_documents(splits, embeddings)
retriever = vs.as_retriever(search_type = "similarity", search_kwargs = {'k': 4})

#4] Prompt template
prompt_template = ChatPromptTemplate.from_messages([
    'system', "Answer only from provided context. If you don't know the answer, say you don't know. Always use all available information to answer the question. Always use all available information to answer the question. Always use all available information to answer the question.",
    'human', 'Question: {question}\n\nContext:\n{context}'
])

#5] Chain
llm = ChatOpenAI(model = "gpt-4o-mini", temperature = 0.5)

def format_text(docs):
    return "\n\n".join(d.page_content for d in docs)

parallel = RunnableParallel(
    {'context': retriever | RunnableLambda(format_text),
     'question': RunnablePassthrough()}
)

chain = parallel | prompt_template | llm | StrOutputParser()


#6] Run
while True:
    print("PDF ready. Ask question: ")
    q = input("\nQ:").strip().lower()

    if q in ["bye", 'thankyou', "exit"]:
        print("\nThankyou have a great day!")
        break

    ans = chain.invoke(q.strip())
    print("\nA: ", ans)
    print("-"*50)

