"""
Streamlit page for knowledge querying with agents, RAG, and vector stores.
"""
import streamlit as st
from typing import List, Dict, Optional
import tempfile
import os
from pathlib import Path

from langchain.embeddings import OpenAIEmbeddings, HuggingFaceEmbeddings
from langchain.vectorstores import Chroma, FAISS, Milvus
from langchain.document_loaders import (
    PyPDFLoader,
    TextLoader,
    Docx2txtLoader,
    UnstructuredMarkdownLoader
)
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.chat_models import ChatOpenAI
from langchain.agents import AgentExecutor, create_openai_functions_agent
from langchain.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain.schema.messages import AIMessage, HumanMessage
from langchain.tools import Tool
from langchain.memory import ConversationBufferMemory

from adpa.ui.utils.state import UIState
from adpa.ui.utils.validation import InputValidator

class KnowledgeQueryApp:
    """Main application class for knowledge querying."""
    
    def __init__(self):
        self.setup_session_state()
        self.setup_embeddings()
        self.setup_vector_stores()
        self.setup_agents()
        
    def setup_session_state(self):
        """Initialize session state variables."""
        UIState.init_session_state()
        
    def setup_embeddings(self):
        """Setup available embedding models."""
        self.embedding_options = {
            'OpenAI': lambda: OpenAIEmbeddings(),
            'HuggingFace (all-MiniLM-L6-v2)': lambda: HuggingFaceEmbeddings(
                model_name="sentence-transformers/all-MiniLM-L6-v2"
            )
        }
    
    def setup_vector_stores(self):
        """Setup available vector stores."""
        self.vector_store_options = {
            'Chroma': lambda docs, embeddings: Chroma.from_documents(
                documents=docs,
                embedding=embeddings,
                persist_directory="./chroma_db"
            ),
            'FAISS': lambda docs, embeddings: FAISS.from_documents(
                documents=docs,
                embedding=embeddings
            ),
            'Milvus': lambda docs, embeddings: Milvus.from_documents(
                documents=docs,
                embedding=embeddings,
                connection_args={"host": "localhost", "port": "19530"}
            )
        }
    
    def setup_agents(self):
        """Setup available agents."""
        self.agent_options = {
            'RAG Agent': self.create_rag_agent,
            'Research Agent': self.create_research_agent,
            'QA Agent': self.create_qa_agent
        }
    
    def create_rag_agent(self, vector_store) -> AgentExecutor:
        """Create a RAG-focused agent."""
        tools = [
            Tool(
                name="Search Documents",
                description="Search through uploaded documents for relevant information",
                func=lambda q: vector_store.similarity_search(q, k=3)
            )
        ]
        
        prompt = ChatPromptTemplate.from_messages([
            ("system", "You are a helpful AI assistant that uses RAG to answer questions. "
                      "Always search the documents first and base your answers on the retrieved content."),
            MessagesPlaceholder(variable_name="chat_history"),
            ("human", "{input}"),
            MessagesPlaceholder(variable_name="agent_scratchpad")
        ])
        
        llm = ChatOpenAI(temperature=0)
        agent = create_openai_functions_agent(llm, tools, prompt)
        return AgentExecutor(agent=agent, tools=tools, verbose=True)
    
    def create_research_agent(self, vector_store) -> AgentExecutor:
        """Create a research-focused agent."""
        tools = [
            Tool(
                name="Search Documents",
                description="Search through documents for research information",
                func=lambda q: vector_store.similarity_search(q, k=5)
            ),
            Tool(
                name="Analyze Content",
                description="Analyze document content for patterns and insights",
                func=lambda q: self.analyze_content(q, vector_store)
            )
        ]
        
        prompt = ChatPromptTemplate.from_messages([
            ("system", "You are a research assistant that analyzes documents deeply. "
                      "Focus on finding patterns, connections, and insights."),
            MessagesPlaceholder(variable_name="chat_history"),
            ("human", "{input}"),
            MessagesPlaceholder(variable_name="agent_scratchpad")
        ])
        
        llm = ChatOpenAI(temperature=0.2)
        agent = create_openai_functions_agent(llm, tools, prompt)
        return AgentExecutor(agent=agent, tools=tools, verbose=True)
    
    def create_qa_agent(self, vector_store) -> AgentExecutor:
        """Create a QA-focused agent."""
        tools = [
            Tool(
                name="Search Documents",
                description="Search through documents for specific answers",
                func=lambda q: vector_store.similarity_search(q, k=2)
            )
        ]
        
        prompt = ChatPromptTemplate.from_messages([
            ("system", "You are a precise QA assistant. Provide direct, accurate answers "
                      "based on the document content. If unsure, say so."),
            MessagesPlaceholder(variable_name="chat_history"),
            ("human", "{input}"),
            MessagesPlaceholder(variable_name="agent_scratchpad")
        ])
        
        llm = ChatOpenAI(temperature=0)
        agent = create_openai_functions_agent(llm, tools, prompt)
        return AgentExecutor(agent=agent, tools=tools, verbose=True)
    
    def analyze_content(self, query: str, vector_store) -> str:
        """Analyze document content for patterns and insights."""
        results = vector_store.similarity_search(query, k=5)
        # Add your custom analysis logic here
        return "Analysis results: " + "\n".join(doc.page_content for doc in results)
    
    def load_document(self, file) -> List[str]:
        """Load and process a document."""
        # Validate file
        is_valid, error = InputValidator.validate_file_upload(
            file,
            allowed_types=['pdf', 'txt', 'docx', 'md'],
            max_size_mb=10
        )
        if not is_valid:
            st.error(error)
            return []

        temp_dir = tempfile.mkdtemp()
        temp_path = os.path.join(temp_dir, file.name)
        
        with open(temp_path, 'wb') as f:
            f.write(file.getvalue())
        
        # Select appropriate loader
        if file.name.endswith('.pdf'):
            loader = PyPDFLoader(temp_path)
        elif file.name.endswith('.txt'):
            loader = TextLoader(temp_path)
        elif file.name.endswith('.docx'):
            loader = Docx2txtLoader(temp_path)
        elif file.name.endswith('.md'):
            loader = UnstructuredMarkdownLoader(temp_path)
        else:
            raise ValueError(f"Unsupported file type: {file.name}")
        
        documents = loader.load()
        
        # Clean up
        os.remove(temp_path)
        os.rmdir(temp_dir)
        
        return documents
    
    def process_documents(self, documents: List[str]) -> List[str]:
        """Process documents with text splitter."""
        text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=1000,
            chunk_overlap=200
        )
        return text_splitter.split_documents(documents)
    
    def render_chat_history(self):
        """Render chat history in Streamlit."""
        for message in UIState.get_chat_history():
            if isinstance(message, HumanMessage):
                st.write(f"🧑 **You:** {message.content}")
            elif isinstance(message, AIMessage):
                st.write(f"🤖 **Assistant:** {message.content}")
    
    def run(self):
        """Run the Streamlit app."""
        st.title("Knowledge Query")
        st.markdown("Upload documents and ask questions using advanced AI agents.")
        
        # File upload
        uploaded_file = st.file_uploader(
            "Upload Document",
            type=['pdf', 'txt', 'docx', 'md'],
            help="Upload a document to query"
        )
        
        if uploaded_file:
            documents = self.load_document(uploaded_file)
            if documents:
                processed_docs = self.process_documents(documents)
                UIState.set('documents', processed_docs)
                st.success(f"Processed {len(processed_docs)} document chunks")
        
        # Vector store selection
        if UIState.get('documents'):
            vector_store_type = st.selectbox(
                "Select Vector Store",
                options=list(self.vector_store_options.keys())
            )
            
            embedding_type = st.selectbox(
                "Select Embedding Model",
                options=list(self.embedding_options.keys())
            )
            
            if st.button("Create Vector Store"):
                embeddings = self.embedding_options[embedding_type]()
                vector_store = self.vector_store_options[vector_store_type](
                    UIState.get('documents'),
                    embeddings
                )
                UIState.set('vector_store', vector_store)
                st.success("Vector store created successfully!")
        
        # Agent selection and query
        if UIState.get('vector_store'):
            agent_type = st.selectbox(
                "Select Agent",
                options=list(self.agent_options.keys())
            )
            
            query = st.text_input("Enter your question")
            
            if query:
                # Validate query
                is_valid, error = InputValidator.validate_query(query)
                if not is_valid:
                    st.error(error)
                    return

                agent = self.agent_options[agent_type](UIState.get('vector_store'))
                UIState.set('agent', agent)
                
                with st.spinner("Thinking..."):
                    response = agent.run(query)
                    UIState.add_to_chat_history("human", query)
                    UIState.add_to_chat_history("ai", response)
            
            # Display chat history
            self.render_chat_history()

if __name__ == "__main__":
    app = KnowledgeQueryApp()
    app.run()
