import streamlit as st 
from dotenv import load_dotenv
from PyPDF2 import PdfReader
from langchain.text_splitter import CharacterTextSplitter
from langchain.embeddings import OpenAIEmbeddings,  HuggingFaceInstructEmbeddings
# FAISS allows you to store your embeddings - in your local storage 
from langchain.vectorstores import FAISS
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationalRetrievalChain
from langchain.chat_models import ChatOpenAI
from htmlTemplates import css, bot_template, user_template
def get_pdf_text(pdf_docs):
    text = ""
    for pdf in pdf_docs:
        pdf_reader = PdfReader(pdf)
        for page in pdf_reader.pages:
            text += page.extract_text()
    return text

def get_text_chunks(raw_pdf_text):
    #divide the extracted text into chuncks
    text_splitter = CharacterTextSplitter(separator="\n", chunk_size=1000, chunk_overlap=200, length_function=len)

    chunks = text_splitter.split_text(raw_pdf_text)
    return chunks

def create_vector_store(text_chunks):
    #embeddings = HuggingFaceInstructEmbeddings(model_name="hkunlp/instructor-xl")
    embeddings = OpenAIEmbeddings()
    vector_store = FAISS.from_texts(texts=text_chunks, embedding=embeddings)
    return vector_store

def get_conversation_chain(vector_store):
    llm = ChatOpenAI()
    memory = ConversationBufferMemory(memory_key='chat_history', return_messages=True)
    conversation_chain = ConversationalRetrievalChain.from_llm(
        llm=llm,
        retriever= vector_store.as_retriever(),
        memory=memory
        )
    return conversation_chain
    

def handle_user_input(user_question):
    response = st.session_state.conversation('question', user_question)
    st.session_state.chat_history = response['chat_history']

    for i, message in enumerate(st.session_state.chat_history):
        if i % 2 == 0 :
            st.write(user_template.replace("{{MSG}}",message.content), unsafe_allow_html=True)
        else:
            st.write(bot_template.replace("{{MSG}}",message.content), unsafe_allow_html=True)


def main():
    load_dotenv()
    st.set_page_config(page_title="Chat With PDFs", page_icon=":books:")

    st.write(css, unsafe_allow_html=True)

    if "conversation" not in st.session_state:
        st.session_state.conversation = None

    if "chat_history" not in st.session_state:
        st.session_state.chat_history = None

    st.header("Chat With PDFs")
    user_question = st.text_input("Ask a question about your documents")

    if user_question:
        handle_user_input(user_question)

    #st.write(user_template.replace("{{MSG}}","Hello Robot. How are you"), unsafe_allow_html=True)
    #st.write(bot_template.replace("{{MSG}}","Hello Robot. How are you"), unsafe_allow_html=True)

    with st.sidebar:
        st.subheader("Your Documents")
        pdf_docs = st.file_uploader("Upload Your PDFs here and click process",accept_multiple_files=True)
        if st.button("Process"):
            with st.spinner("Processing"):

                #get text from pdfs 
                raw_pdf_text = get_pdf_text(pdf_docs)

                #get the text chunks
                text_chunks = get_text_chunks(raw_pdf_text)

                #create vector store
                vector_store = create_vector_store(text_chunks)

                #create conversation chain
                st.session_state.conversation = get_conversation_chain(vector_store)


    

main()
