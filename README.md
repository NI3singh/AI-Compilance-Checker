# Compliance Checker

The **Compliance Checker** is an AI-driven application designed to analyze and verify contract compliance by performing vector-based similarity searches. It leverages PostgreSQL with **pgvector** for efficient vector searches and document embeddings, providing a robust, open-source solution to manage both structured and unstructured data.

---

## **Key Features**
- **Efficient Vector Search**: Perform faster similarity queries with advanced indexing techniques.
- **Unified Database**: Manage relational and vector data in one system seamlessly.
- **AI-Enhanced Analysis**: Utilize OpenAI models for generating and comparing document embeddings.
- **Open Source**: Transparent and cost-effective for all use cases.

---

## **Prerequisites**
Ensure the following dependencies are installed before proceeding:
- **Docker**: For containerized deployment.
- **Python 3.10**: For running the application backend.
- **PostgreSQL**: For managing and storing document vectors.
- **OpenAI API Key**: For embedding generation using OpenAI models.
- **PostgreSQL GUI Client** (optional, e.g., TablePlus): To interact with the database.

---

## **Setup Instructions**

### **1. Clone the Repository**
Clone the project to your local machine:
```bash
git clone https://github.com/Ishita0211/compliance-checker.git
cd compliance-checker
