## 📜 LSTM Next Word Predictor  

### 🔥 Overview  
This project is a **Next Word Prediction** model built using **LSTM (Long Short-Term Memory)** neural networks. The model takes an input sequence of words and predicts the most probable next word. It is trained on Shakespeare's *Hamlet* and is deployed using **Streamlit** for an interactive experience.  

---

## 🚀 Features  
✅ **LSTM-based Prediction:** Uses a trained deep learning model to predict the next word.  
✅ **Pre-trained Tokenizer:** A pre-trained tokenizer processes input text sequences for accurate predictions.  
✅ **Streamlit UI:** Simple and interactive web-based interface for easy testing.  
✅ **Pickle-based Model Storage:** Efficient serialization of the tokenizer for reusability.  

---

## 📂 Project Structure  
```
LSTM-NextWord-Predictor/
│── main.py               # Streamlit app for next-word prediction
│── requirements.txt      # Dependencies list
│── hamlet.h5             # Pre-trained LSTM model
│── tokenize.pickle       # Tokenizer for text preprocessing
│── experiments.ipynb     # Jupyter notebook for experimentation and training the model
│── README.md             # Project documentation
```

---

## 🛠 Installation & Setup  

### 1️⃣ Clone the Repository  
```bash
git clone https://github.com/Vansh3140/LSTM-NextWord-Predictor.git
cd LSTM-NextWord-Predictor
```

### 2️⃣ Install Dependencies  
Ensure you have Python **3.10+** installed. Then, install required packages:  
```bash
pip install -r requirements.txt
```

### 3️⃣ Run the Streamlit App  
```bash
streamlit run main.py
```
Now, open the **localhost link** in your browser to use the Next Word Predictor.

---

## ⚡ How It Works  
1️⃣ **Enter a sequence of words** in the input box.  
2️⃣ **Click on the "Predict Next" button** to see the predicted word.  
3️⃣ The LSTM model processes the sequence and returns the most probable next word.  

---

## 🧠 How the Model Works  
- The LSTM model is trained on **Shakespeare's *Hamlet***, learning to predict words based on historical text sequences.  
- The tokenizer preprocesses text, converting words into sequences for model interpretation.  
- Predictions are made by analyzing the input sequence and selecting the word with the highest probability.  

---

## 📌 Dependencies  
- Python 3.10+  
- TensorFlow  
- NumPy  
- Streamlit  
- Pickle  
- Keras  

Install them using:  
```bash
pip install tensorflow numpy streamlit
```

---

## 🤖 Future Improvements  
📌 Extend training to modern English datasets.  
📌 Implement Beam Search for better predictions.  
📌 Deploy as a live web app using **Streamlit Sharing / Hugging Face Spaces**.  

---

## ✨ Contribution  
Feel free to fork this repo, open issues, and submit PRs. 🚀  

---

## 📜 License  
This project is open-source under the **MIT License**.  

---

This README gives your project a **professional** and **engaging** touch while making it easy for contributors to set up and understand. 🚀 Let me know if you want any changes!
