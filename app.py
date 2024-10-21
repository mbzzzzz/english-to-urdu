import streamlit as st
from transformers import pipeline, AutoTokenizer, AutoModelForCausalLM

# Load the translation pipeline
pipe = pipeline("text-generation", model="Alisaeed001/Llama-2-7b-chat-finetune")

# Load the model and tokenizer directly
tokenizer = AutoTokenizer.from_pretrained("Alisaeed001/Llama-2-7b-chat-finetune")
model = AutoModelForCausalLM.from_pretrained("Alisaeed001/Llama-2-7b-chat-finetune")

# Streamlit app layout
st.title("English to Roman Urdu Chatbot")
st.write("Enter English text below and click the button to generate a response in Roman Urdu.")

# Text input
english_text = st.text_area("Input English Text")

# Button for translation
if st.button("Generate"):
    if english_text:
        # Generate Roman Urdu response
        response = pipe(english_text, max_length=100, num_return_sequences=1)[0]['generated_text']
        
        # Display result
        st.subheader("Generated Response:")
        st.write(response)
    else:
        st.error("Please enter some English text.")
