import streamlit as st
from src.services.ingestion_manager import FileIngestionManager
from src.utils.similarity_search import similarity_search

# Initialize FileIngestionManager
ingestion_manager = FileIngestionManager()

# Streamlit app
st.title("Compliance Checker")

# Sidebar for file upload
st.sidebar.header("Upload PDF")
uploaded_file = st.sidebar.file_uploader("Choose a PDF file", type="pdf")

if uploaded_file is not None:
    # Save and process the file
    with st.spinner("Processing PDF..."):
        file_path = ingestion_manager.save_file(uploaded_file)
        st.sidebar.success("File successfully uploaded and processed!")

# Search functionality
st.header("Search Contracts")
query = st.text_input("Enter your query:")
top_k = st.slider("Number of results to return", min_value=1, max_value=10, value=5)

if query:
    with st.spinner("Searching..."):
        results = similarity_search(query, top_k)
        if results:
            st.success(f"Found {len(results)} results:")
            for result in results:
                st.subheader(result["document_name"])
                st.write(f"**Parties:** {result['parties']}")
                st.write(f"**Agreement Date:** {result['agreement_date']}")
                st.write(f"**Expiration Date:** {result['expiration_date']}")
                st.write(f"**Question:** {result['question']}")
                st.write(f"**Answer:** {result['answer']}")
                st.write(f"**Category:** {result['category']}")
                st.write("---")
        else:
            st.warning("No results found.")