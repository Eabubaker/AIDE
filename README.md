# AIDE


---

<p align="center">
  <span style="background: linear-gradient(45deg, #12c2e9, #c471ed, #f64f59); -webkit-background-clip: text; -webkit-text-fill-color: transparent;">
    <strong>Prepared by <a href="www.linkedin.com/in/eabubaker"> Emad Abubaker</a></strong>
  </span>
</p>

# AIDE - Audit Intelligence & Document Explorer
## Day 1: Setting the Stage & Our First "Hello AIDE!"

Welcome to Day 1 of building AIDE! Today, our goal is to set up our basic toolkit and create the very first visual part of our application. We'll be using **Streamlit**, a fantastic Python library that lets us build web apps easily.

Think of today as laying the foundation for our smart assistant's "face".

### Prerequisites
* Python 3.8+ installed.
* Pip (Python package installer) installed.

### Setup
1.  Create a project directory (e.g., `aide_project`).
2.  Inside the project directory, create a new Python file, for example, `app.py`.
3.  Install Streamlit:
    ```bash
    pip install streamlit
    ```

### Code (`app.py`)
```python
import streamlit as st

def main():
    st.set_page_config(page_title="AIDE - Audit Assistant", layout="wide")

    st.title("🚀 AIDE - Audit Intelligence & Document Explorer")
    st.subheader("Welcome! Let's build our smart assistant for auditors, step by step.")

    st.sidebar.success("Navigation")
    st.sidebar.info("We are on Day 1: Setup!")

    st.write("""
    This is the beginning of our AIDE application.
    Over the next few days, we will add functionalities like:
    - Document loading
    - Text processing
    - AI-powered Q&A
    """)

if __name__ == "__main__":
    main()
