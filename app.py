import streamlit as st
from transformers import pipeline, AutoTokenizer, AutoModelForCausalLM

# Load the translation pipeline
pipe = pipeline("text-generation", model="Alisaeed001/Llama-2-7b-English-RomanUrdu-finetune")

# Load the model and tokenizer directly
tokenizer = AutoTokenizer.from_pretrained("Alisaeed001/Llama-2-7b-English-RomanUrdu-finetune")
model = AutoModelForCausalLM.from_pretrained("Alisaeed001/Llama-2-7b-English-RomanUrdu-finetune")

# Streamlit app layout
st.title("English to Roman Urdu Translation")
st.write("Enter English text below and click the button to translate it to Roman Urdu.")

# Text input
english_text = st.text_area("Input English Text")

# Button for translation
if st.button("Translate"):
    if english_text:
        # Generate Roman Urdu translation
        translated_text = pipe(english_text, max_length=100, num_return_sequences=1)[0]['generated_text']
        
        # Display result
        st.subheader("Translated Text:")
        st.write(translated_text)
    else:
        st.error("Please enter some English text to translate.")
