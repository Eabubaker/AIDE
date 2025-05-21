# AIDE - Audit Intelligence & Document Explorer

**Prepared by @Emad Abubaker**

Welcome to **AIDE**, an open-source AI-powered assistant designed to revolutionize internal auditing. AIDE enables auditors to query complex company documents (e.g., policies, procedures, contracts, and Global Internal Audit Standards) and receive accurate, context-aware, source-referenced answers in seconds. Powered by Retrieval-Augmented Generation (RAG), AIDE streamlines auditing tasks for professionals, even those without deep technical expertise.

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
- Setting up the environment to create the first visual component of our assistant.

This is the "foundation" for AIDE’s intelligent interface, where auditors will interact with the system.

### Prerequisites

Ensure the following are installed on your **Windows** machine:

1. **Python 3.8+**:
   - Download from [python.org](https://www.python.org/downloads/).
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
   - Download from [git-scm.com](https://git-scm.com/downloads).
   - Verify with:
     ```bash
     git --version
     ```

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

3. **Install Required Packages**:
   - The project requires the following Python packages (listed in `requirements.txt`):
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
   - Install them using:
     ```bash
     pip install -r requirements.txt
     ```

   - If issues arise, ensure `pip` is updated:
     ```bash
     python -m pip install --upgrade -r requirements.txt
     ```

### Testing Your Setup

1. Create a simple Python script (e.g., `app.py`) to verify the environment:
   ```python
   print("Hello, AIDE! Your auditing assistant is ready to grow.")
   ```

2. Run the script:
   ```bash
   python app.py
   ```

This confirms that Python and the required packages are installed correctly. In the next steps, we’ll build AIDE’s interface and knowledge base.

### Troubleshooting

- **Python not found**: Reinstall Python and ensure "Add to PATH" is checked.
- **Pip errors**: Update `pip` using `python -m pip install --upgrade pip`.
- **Package conflicts**: Use a clean virtual environment to avoid conflicts.

### Project Structure

```
AIDE/
├── aide_env/              # Virtual environment
├── app.py                 # Main application script
├── requirements.txt       # List of required packages
├── README.md              # Project documentation
└── LICENSE                # MIT License file
```

### Next Steps

Follow the upcoming phases:
- **Day 2**: Collect and organize documents to build AIDE’s knowledge base.
- **Day 3**: Integrate an AI model to process and answer queries.
- **Day 4**: Design an interactive interface for auditors.

Check the [GitHub repository](https://github.com/Eabubaker/AIDE) for updates and detailed guides.

### Contributing

AIDE is open-source, and we welcome contributions! To contribute:
1. Fork the repository: [https://github.com/Eabubaker/AIDE](https://github.com/Eabubaker/AIDE).
2. Create a new branch (`git checkout -b feature/your-feature`).
3. Commit your changes (`git commit -m "Add your feature"`).
4. Push to the branch (`git push origin feature/your-feature`).
5. Open a Pull Request.

Your feedback and ideas will help make AIDE a powerful tool for the auditing community!

### License

This project is licensed under the MIT License. See the `LICENSE` file for details.

---

**Join the Journey!**  
Follow along on [LinkedIn](https://www.linkedin.com/in/eabubaker) for daily updates on building AIDE. Let’s create a smarter auditing future together! 🚀

