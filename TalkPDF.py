import streamlit as st
from PyPDF2 import PdfReader
from langchain.text_splitter import RecursiveCharacterTextSplitter
import os

from langchain_google_genai import GoogleGenerativeAIEmbeddings
import google.generativeai as  genai
from langchain.vectorstores import FAISS
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.chains.question_answering import load_qa_chain
from langchain.prompts import PromptTemplate
from dotenv import load_dotenv

load_dotenv()

genai.configure(api_key=os.getenv('GOOGLE_API_KEY'))

def get_pdf_text(pdf_docs):
    text=""
    for pdf in pdf_docs:
        pdf_Reader = PdfReader(pdf)
        for page in pdf_Reader.pages:
            text += page.extract_text()
    return text

def get_text_chunks(text):
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,chunk_overlap=200
        )
    chunks = text_splitter.split_text(text)
    return chunks

def get_vectorstore(text_chunks):
    embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001")
    vectorstore = FAISS.from_texts(texts=text_chunks,embedding=embeddings)
    vectore.save_local("faiss_index")
    return vectorstore

def get_conversational_chain():
    prompt_template="""
    Answer the question as detailed as possible from the provided context, make sure to provide all the details. If the answer is not 
    in the provided context just say, "answer is not avaiable in the given context", don't provide the wrong answer\n\n
    Contextt:\n {context}\n
    Question: \n{question}\n
    
    Answer:
    """
    model = ChatGoogleGenerativeAI(model="gemini-pro",temperature=0.3)
    
    PromptTemplate(template=prompt_template, input_variables=["context","question"])
    chain = load_qa_chain(model,chain_type="stuff", prompt = prompt_template)
    return chain

def user_input(user_question):
    embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001")
    
    new_db = FAISS.load_local("faiss_index", embeddings)
    docs = new_db.similarity_search(user_question)
    
    chain = get_conversational_chain()
    
    resposne = chain(
        {"input_documents":docs,"question":user_question}
        , return only putputs=True)
    
    print(resposne)
    st.write("reply: ",resposne["output_text"])
    

def main():
    st.set_page_config("My Gemini interactive PDF chat APP")
    st.header("Chat with multiple PDF using gemini ")
    
    user_question = st.text_input("Ask a question from the PDF files")
    
    if user_question:
        user_input(user_question)
        
    with st.sidebar:
        st.title("Menu: ")
        pdf_docs = st.file_uploader("Upload your PDF files here and Cick on Process",accept_multiple_files=True)
        if st.button("Process"):
            with st.spinner("Processing..."):
                raw_text = get_pdf_text(pdf_docs)
                text_chunks = get_text_chunks(raw_text)
                get_vectorstore(text_chunks)
                st.success("Processing Completed")


if __name__ == "__main__":
    main()
