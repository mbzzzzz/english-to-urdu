import streamlit as st
from transformers import pipeline, AutoTokenizer, AutoModelForSeq2SeqLM

# Load the translation pipeline
pipe = pipeline("text2text-generation", model="ZainAli60/English-to-Urdu")

# Load the model and tokenizer directly
tokenizer = AutoTokenizer.from_pretrained("ZainAli60/English-to-Urdu")
model = AutoModelForSeq2SeqLM.from_pretrained("ZainAli60/English-to-Urdu")

# Streamlit app layout
st.title("English to Urdu Translation")
st.write("Enter English text below and click the button to translate it to Urdu.")

# Text input
english_text = st.text_area("Input English Text")

# Button for translation
if st.button("Translate"):
    if english_text:
        # Generate Urdu translation
        translated = pipe(english_text, max_length=100, num_return_sequences=1)[0]['generated_text']
        
        # Display result
        st.subheader("Translated Text:")
        st.write(translated)
    else:
        st.error("Please enter some English text to translate.")
