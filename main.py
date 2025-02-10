import pickle
import numpy as np
import streamlit as st
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.sequence import pad_sequences


model = load_model("hamlet.h5")

with open("tokenize.pickle", "rb") as file:
    tokenizer = pickle.load(file)

def predict_next_word(model, tokenizer, text, max_sequence_len):
    text_sequence = tokenizer.texts_to_sequences([text])[0]
    if len(text_sequence)>=max_sequence_len:
        text_sequence = text_sequence[-(max_sequence_len-1):]
    text_sequence = pad_sequences([text_sequence], padding='pre', maxlen=max_sequence_len-1)
    predicted = model.predict(text_sequence, verbose=0)
    predicted_word_index = np.argmax(predicted, axis=1)
    for word, index in tokenizer.word_index.items():
        if index==predicted_word_index:
            return word
    return None

st.title("Next Word prediction with LSTM")
input_text = st.text_input("Enter the sequence of words")
if st.button("Predict Next Button"):
    st.write(f"Input sentence :- {input_text}")
    max_sequence_len = model.input_shape[1]
    output_word = predict_next_word(model, tokenizer, input_text, max_sequence_len)
    st.write(f"Next word :- {output_word}")