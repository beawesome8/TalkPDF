# TalkPDF 📄💬

An app that lets you interact with PDFs to obtain data from them.

TalkPDF is an interactive application that allows users to upload multiple PDF files and ask questions about their content. The app uses Google Generative AI and LangChain to process the PDFs and provide detailed answers based on the text within the documents.

## Features ✨

- 📁 Upload multiple PDF files
- 📝 Extract text from PDFs
- 📏 Split text into manageable chunks
- 🗂️ Create a vector store for efficient text search
- ❓ Ask questions and get detailed answers based on the PDF content

## Requirements 📋

To run this application, you need the following Python packages:

- `streamlit`
- `google-generativeai`
- `python-dotenv`
- `langchain`
- `PyPDF2`
- `faiss-cpu`
- `langchain_google_genai`

You can install the required packages using the following command:

```sh
pip install -r requirements.txt
Setup 🛠️
Clone the repository to your local machine.

Create a .env file in the root directory and add your Google API key:

sh
GOOGLE_API_KEY=your_api_key
Install the required packages:

sh
pip install -r requirements.txt
Usage 🚀
Run the app using the following command:

sh
streamlit run TalkPDF.py
Upload your PDF files using the sidebar menu.

Ask questions about the content of the uploaded PDFs using the text input field.

How It Works 🔍
Upload PDFs: Users can upload multiple PDF files through the sidebar.

Process PDFs: The app extracts text from the PDFs and splits it into chunks.

Create Vector Store: The text chunks are embedded and stored in a FAISS vector store for efficient similarity search.

Ask Questions: Users can ask questions about the PDF content, and the app will provide detailed answers based on the extracted text.

Libraries Used 📚
Streamlit: Used for creating the web application interface.

google-generativeai: Provides access to Google Generative AI for embeddings and conversational models.

python-dotenv: Loads environment variables from a .env file.

LangChain: Used for text processing, splitting, and creating conversational chains.

PyPDF2: Extracts text from PDF files.

faiss-cpu: Efficient similarity search and clustering of dense vectors.

langchain_google_genai: Integrates LangChain with Google Generative AI for embedding and conversational models.

License ⚖️
This project is licensed under the MIT License. See the LICENSE file for details.

Acknowledgements 🙏
Streamlit

LangChain

Google Generative AI

Enjoy using TalkPDF! 🎉
