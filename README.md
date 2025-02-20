# ChatWithPDF 📄💬

An app that lets you interact with PDFs to obtain data from them.

ChatWithPDF is an interactive application that allows users to upload multiple PDF files and ask questions about their content. The app uses Google Generative AI and LangChain to process the PDFs and provide detailed answers based on the text within the documents.

## Features ✨

- 📁 Upload multiple PDF files
- 📝 Extract text from PDFs
- 📏 Split text into manageable chunks
- 🗂️ Create a vector store for efficient text search
- ❓ Ask questions and get detailed answers based on the PDF content

## Requirements 📋

## To run this application, you need the following Python packages:

- `streamlit`
- `google-generativeai`
- `python-dotenv`
- `langchain`
- `PyPDF2`
- `faiss-cpu`
- `langchain_google_genai`

## You can install the required packages using the following command:

pip install -r requirements.txt

## Setup 🛠️
1. Clone the repository to your local machine.

2.Create a .env file in the root directory and add your Google API key:

GOOGLE_API_KEY=your_api_key

3.Install the required packages:

pip install -r requirements.txt

## Usage 🚀

1.Run the app using the following command: streamlit run ChatWithPDF.py

2.Upload your PDF files using the sidebar menu.

3.Ask questions about the content of the uploaded PDFs using the text input field.

## How It Works 🔍
1.Upload PDFs: Users can upload multiple PDF files through the sidebar.

2.Process PDFs: The app extracts text from the PDFs and splits it into chunks.

3.Create Vector Store: The text chunks are embedded and stored in a FAISS vector store for efficient similarity search.

4.Ask Questions: Users can ask questions about the PDF content, and the app will provide detailed answers based on the extracted text.

## Libraries Used 📚
-Streamlit: Used for creating the web application interface.

-google-generativeai: Provides access to Google Generative AI for embeddings and conversational models.

-python-dotenv: Loads environment variables from a .env file.

-LangChain: Used for text processing, splitting, and creating conversational chains.

-PyPDF2: Extracts text from PDF files.

-faiss-cpu: Efficient similarity search and clustering of dense vectors.

-langchain_google_genai: Integrates LangChain with Google Generative AI for embedding and conversational models.

## License ⚖️
This project is licensed under the MIT License and can be used and modified if required.

## Acknowledgements 🙏
Streamlit

LangChain

Google Generative AI

Enjoy using TalkPDF! 🎉
