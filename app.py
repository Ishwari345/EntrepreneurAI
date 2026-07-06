# app.py
import streamlit as st
from gpt4all import GPT4All
import os
from datetime import datetime
import time

# ----------- Streamlit Page Config -----------
st.set_page_config(
    page_title="💼 Entrepreneur Bot",
    page_icon="💡",
    layout="wide"
)

# ----------- Header -----------
st.markdown(
    """
    <div style="background-color:#4CAF50;padding:20px;border-radius:10px">
        <h1 style="color:white;text-align:center;">💼 Entrepreneur Bot</h1>
        <p style="color:white;text-align:center;">Ask entrepreneurship-related questions and get answers based on your PDFs!</p>
    </div>
    """, unsafe_allow_html=True
)Microsoft.QuickAction.BatterySaver

# ----------- Sidebar -----------
st.sidebar.header("Settings & PDFs")

model_path = st.sidebar.text_input(
    "Local GPT4All model path",
    value=r"C:\Users\ishwa\AppData\Local\nomic.ai\GPT4All\orca-mini-3b-gguf2-q4_0.gguf"
)

if not os.path.exists(model_path):
    st.sidebar.error("⚠️ Model file not found. Check the path!")

uploaded_files = st.sidebar.file_uploader(
    "Upload PDFs (multiple allowed)", type=["pdf"], accept_multiple_files=True
)

# ----------- Load Model -----------
@st.cache_resource(show_spinner=True)
def load_model(path):
    return GPT4All(path)

if os.path.exists(model_path):
    st.sidebar.success("✅ Model loaded successfully!")
    model = load_model(model_path)
else:
    st.warning("Please provide a valid model path.")
    st.stop()

# Simulate PDF reading
if uploaded_files:
    st.sidebar.info("📚 Reading your PDFs...")
    pdf_texts = []
    for pdf in uploaded_files:
        pdf_texts.append(pdf.read().decode("utf-8", errors="ignore"))
    st.sidebar.success("✅ PDFs loaded!")

# ----------- Chat History -----------
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# ----------- Chat Input -----------
with st.form(key="chat_form", clear_on_submit=True):
    user_input = st.text_input("Type your question here...", "")
    submitted = st.form_submit_button("Ask")
    if submitted and user_input:
        st.session_state.chat_history.append({
            "role": "user",
            "content": user_input,
            "time": datetime.now().strftime("%H:%M:%S")
        })
        # Animated loader
        with st.spinner("Bot is thinking... 🤔"):
            time.sleep(1)  # optional delay for realism
            response = model.generate(user_input)
        st.session_state.chat_history.append({
            "role": "bot",
            "content": response,
            "time": datetime.now().strftime("%H:%M:%S")
        })

# ----------- Display Chat with Styles -----------
st.markdown("<hr>", unsafe_allow_html=True)
for chat in st.session_state.chat_history:
    if chat["role"] == "user":
        st.markdown(
            f"""
            <div style='text-align:right; padding:10px 0;'>
                <div style='display:inline-block; background-color:#DCF8C6; color:black; padding:10px 15px; border-radius:15px; max-width:70%;'>
                    <b>You:</b> {chat['content']}<br><small style='color:gray;'>{chat['time']}</small>
                </div>
            </div>
            """, unsafe_allow_html=True
        )
    else:
        st.markdown(
            f"""
            <div style='text-align:left; padding:10px 0;'>
                <div style='display:inline-block; background-color:#F1F0F0; color:black; padding:10px 15px; border-radius:15px; max-width:70%;'>
                    <b>Bot:</b> {chat['content']}<br><small style='color:gray;'>{chat['time']}</small>
                </div>
            </div>
            """, unsafe_allow_html=True
        )

# ----------- Clear Chat Button -----------
st.markdown("<hr>", unsafe_allow_html=True)
if st.button("🗑️ Clear Chat"):
    st.session_state.chat_history = []
    st.rerun()

# ----------- Footer -----------
st.markdown(
    """
    <div style="text-align:center; color:gray; padding:10px;">
        Built with 💡 <b>GPT4All</b> and <b>Streamlit</b>
    </div>
    """, unsafe_allow_html=True
)
