# AIDE - Audit Intelligence & Document Explorer

**Prepared by @Emad Abubaker**

Welcome to **AIDE**, an open-source AI-powered assistant designed to transform internal auditing. AIDE enables auditors to query complex company documents (e.g., policies, procedures, contracts, and Global Internal Audit Standards) and receive accurate, context-aware, source-referenced answers in seconds. Powered by Retrieval-Augmented Generation (RAG), AIDE streamlines auditing tasks for professionals, even those without deep technical expertise.

This `README.md` guides you through **Day 1** of building AIDE, where we set up the development environment on a **Windows** system and lay the foundation for our smart assistant.

## Project Overview

AIDE (Audit Intelligence & Document Explorer) aims to:

- Provide a user-friendly interface for auditors to ask questions about company documents.
- Deliver precise, context-aware answers with source references.
- Leverage open-source tools to make auditing smarter and more efficient.

The project is structured in **3 phases**:

1. **Data Preparation**: Building a knowledge base from documents.
2. **AI Integration**: Connecting a language model to process queries.
3. **Interface Design**: Creating an interactive user interface.

## Day 1: Setting the Stage & Building the Foundation

Today, we focus on:

- Installing the necessary tools to build AIDE.
- Setting up the environment to create the first component of our assistant.

This is the "foundation" for AIDE’s intelligent interface, where auditors will interact with the system.

### Prerequisites

Ensure the following are installed on your **Windows** machine:

1. **Python 3.8+**:

   - Download from python.org.
   - Check "Add Python to PATH" during installation.
   - Verify with:

     ```bash
     python --version
     ```

2. **Pip (Python Package Installer)**:

   - Included with Python. Update to the latest version:

     ```bash
     python -m pip install --upgrade pip
     ```

3. **Git** (optional, for cloning the repository):

   - Download from git-scm.com.
   - Verify with:

     ```bash
     git --version
     ```

4. **Ollama**:

   - Ollama enables running local language models, which we’ll use for AI integration.
   - Installation steps:
     1. Download the Windows installer from ollama.com.
     2. Run the installer and follow the prompts.
     3. Verify installation:

        ```bash
        ollama --version
        ```
     4. Pull a model (e.g., LLaMA) to test:

        ```bash
        ollama pull llama3
        ```

### Tool Descriptions

The following table lists the tools and packages required for AIDE, along with their purpose:

| **Tool/Package** | **Purpose** |
| --- | --- |
| **Python 3.8+** | Core programming language for running AIDE’s scripts and dependencies. |
| **Pip** | Manages installation of Python packages listed in `requirements.txt`. |
| **Git** | Optional tool for cloning the AIDE repository and managing version control. |
| **Ollama** | Runs local language models for secure, offline AI processing in AIDE. |
| **streamlit** | Builds the interactive web interface for AIDE’s user queries. |
| **langchain** | Facilitates integration of language models with document data for RAG. |
| **langchain-community** | Provides community extensions for LangChain (e.g., tools, integrations). |
| **sentence-transformers** | Generates embeddings to convert documents into machine-readable formats. |
| **deepseek** | Enhances AI model capabilities for processing complex queries. |
| **chromadb** | Manages vector storage for efficient document retrieval in RAG. |
| **tqdm** | Displays progress bars for data processing tasks. |
| **truststore** | Ensures secure SSL connections for external API calls (if needed). |

### Installation Steps

1. **Clone the AIDE Repository**:

   ```bash
   git clone https://github.com/Eabubaker/AIDE.git
   cd AIDE
   ```

2. **Create a Virtual Environment** (recommended):

   ```bash
   python -m venv aide_env
   .\aide_env\Scripts\activate
   ```

3. **Install Python Packages**:

   - Use the `requirements.txt` file:

     ```
     streamlit==1.29.0
     langchain==0.1.17
     langchain-community==0.0.23
     sentence-transformers==2.2.0
     deepseek==0.1.0
     chromadb==0.4.16
     tqdm==4.66.1
     truststore==0.3.3
     ```

   - Install with:

     ```bash
     pip install -r requirements.txt
     ```

   - If issues arise, update `pip`:

     ```bash
     python -m pip install --upgrade -r requirements.txt
     ```

4. **Set Up Ollama**:

   - After installing Ollama, test it by running a model:

     ```bash
     ollama run llama3
     ```
   - This prepares the local AI model for later integration.

### Testing Your Setup

1. Create a simple Python script (e.g., `app.py`) to verify the environment:

   ```python
   print("Hello, AIDE! Your auditing assistant is ready to grow.")
   ```

2. Run the script:

   ```bash
   python app.py
   ```

3. Test Ollama:

   ```bash
   ollama run llama3 "Hello, AIDE!"
   ```

This confirms that Python, the required packages, and Ollama are installed correctly.

### Troubleshooting

- **Python not found**: Reinstall Python and ensure "Add to PATH" is checked.
- **Pip errors**: Update `pip` using `python -m pip install --upgrade pip`.
- **Ollama errors**: Ensure Ollama is installed and the model (e.g., `llama3`) is pulled successfully.
- **Package conflicts**: Use a clean virtual environment to avoid conflicts.

### Project Structure

```
AIDE/
├── aide_env/              # Virtual environment
├── app.py                 # Main application script
├── requirements.txt       # List of required Python packages
├── README.md              # Project documentation
└── LICENSE                # MIT License file
```

### Next Steps

Follow the upcoming phases:

- **Day 2**: Collect and organize documents to build AIDE’s knowledge base.
- **Day 3**: Integrate an AI model to process and answer queries.
- **Day 4**: Design an interactive interface for auditors.

Check the GitHub repository for updates and detailed guides.

Your feedback and ideas will help make AIDE a powerful tool for the auditing community!

### 

---

**Join the Journey!**  
Follow along on [LinkedIn](https://www.linkedin.com/in/eabubaker) for daily updates on building AIDE. Let’s create a smarter auditing future together! 🚀

