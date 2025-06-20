# Health-chatbot
An AI-powered web chatbot that provides conversational support for general health and wellness queries. It uses a hybrid system combining predefined question-answer pairs with large language model (LLM) responses via the Groq API.

## 🚀 Features

- ✅ **Hybrid Response System**  
  Uses predefined prompt-response pairs for common queries and falls back to LLM-generated answers when needed.

- ✅ **Multiple Model Support**  
  Switch between LLaMA3 and Mixtral models in real time via a dropdown selector.

- ✅ **Session-Based Chat Memory**  
  Maintains conversation context during the session.

- ✅ **Downloadable Chat Log**  
  Users can export their chat history as a `.txt` file.

- ✅ **Responsive UI**  
  Styled with Bootstrap for a clean and mobile-friendly experience.

---

## 🛠 Tech Stack

**Frontend:**  
- HTML, CSS (Bootstrap), JavaScript

**Backend:**  
- Python, Flask, Pandas  
- LangChain + Groq API (LLaMA3, Mixtral)

**ML Models:**  
- [Groq LLaMA3](https://groq.com/)  
- [Groq Mixtral](https://groq.com/)

---

# Setup
1. Install the required packages:
```bash
  pip install -r requirements.txt
```
2. Run the application:
```bash
  python app.py
```
