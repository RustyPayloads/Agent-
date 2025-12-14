# Simple Web-Searching AI Agent

A minimalist Python agent built using the Google Gemini API and the `google:search` tool, following the ReAct (Reasoning + Acting) pattern.

## 🚀 Setup & Installation

1.  **Clone the Repository:**
    ```bash
    git clone [your_repo_link]
    cd simple_agent_repo
    ```

2.  **Create and Activate Virtual Environment:**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```

3.  **Install Dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Configure API Key:**
    Create a file named `.env` in the root directory and add your API key:
    ```
    # .env
    GEMINI_API_KEY="YOUR_API_KEY_HERE"
    ```

## 🧠 Usage

Run the entry point script:

```bash
python run.py
