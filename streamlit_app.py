import streamlit as st
import pickle
import os

# --- PAGE CONFIGURATION ---
st.set_page_config(page_title="SMS Spam Detector", page_icon="📩")

# --- MODEL LOADING ---
# This function ensures the model is only loaded into memory once
@st.cache_resource
def load_model():
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    # Adjust "model" folder name if your .pkl is in the root
    MODEL_PATH = os.path.join(BASE_DIR, "model", "spam_model.pkl") 
    
    try:
        with open(MODEL_PATH, "rb") as f:
            return pickle.load(f)
    except FileNotFoundError:
        st.error(f"Model file not found at {MODEL_PATH}. Please check your directory structure.")
        return None

model = load_model()

# --- USER INTERFACE ---
st.title("📩 SMS Spam Detection System")
st.markdown("This application uses a **Naive Bayes** model to classify messages.")

message = st.text_area("Enter the SMS text below:", placeholder="e.g., Free entry in 2 a wkly comp to win FA Cup final...")

if st.button("Analyze Message"):
    if model is not None:
        if message.strip():
            # Prediction logic
            prediction = model.predict([message])[0]
            
            st.divider()
            if prediction == 1:
                st.error("### 🚨 Result: SPAM")
                st.warning("This message contains patterns common in fraudulent or promotional texts.")
            else:
                st.success("### ✅ Result: HAM (Safe)")
                st.info("This looks like a normal, safe message.")
        else:
            st.warning("Please enter some text first.")
    else:
        st.error("Model is not loaded. Cannot perform prediction.")

# --- SIDEBAR INFO ---
st.sidebar.title("App Details")
st.sidebar.info("Built with Streamlit & Scikit-learn.")
st.sidebar.write(f"**Dataset:** Kaggle SMS Spam Collection")
