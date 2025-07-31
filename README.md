# 🧠 Customer Churn Predictor

An advanced deep learning-powered web application that predicts whether a customer is likely to churn using an Artificial Neural Network (ANN) model.

-✅ Binary Classification
-✅ Trained on Customer Churn Data
-✅ Built with TensorFlow and Streamlit

Built with Python and Streamlit, the app enables businesses to understand churn behavior and act proactively.


## 🚀 Features

* Predict if a customer is likely to **Churn or Stay**
* User-friendly interface with input fields for:
  * Credit Score,	Geography, Gender,	Age, Tenure, Balance
  * Num Of Products,	Has CrCard,	Is Active Member,	Estimated Salary
* Real-time prediction on user input


<!--
## 🎥 Screen Recording

* [📺 Source Code](https://github.com/itsBabuaa/Customer-Churn-ANN-Classification)
* [📺 Live Demo](https://youtu.be/h7CiaXpHkFI) *(Replace with actual demo link if available)*
-->

## 🧠 Model Details

* **Algorithm**: Artificial Neural Network (ANN)
* **Framework**: TensorFlow & Keras
* **Training**:

  * Input features: 7+
  * Target: `Churn` (Yes/No)
  * Preprocessing includes one-hot encoding and feature scaling
* Model achieves high precision and recall in churn detection


## 🛠️ Tech Stack

* Python 3.11
* Pandas, NumPy
* TensorFlow, Keras
* scikit-learn
* Streamlit for UI


## 🔧 How to Run

1. Clone the repository:

   ```bash
   git clone https://github.com/itsBabuaa/Customer-Churn-ANN-Classification.git
   cd Customer-Churn-ANN-Classification
   ```

2. Create a virtual environment:

   ```bash
   python -m venv .venv
   source .venv/bin/activate  # Windows: .venv\Scripts\activate
   ```

3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Launch the app:

   ```bash
   streamlit run app.py
   ```


## 🙏 Acknowledgments
* Thanks to open-source contributors for frameworks like TensorFlow and Streamlit


👨‍💻 Developed by [@itsBabuaa](https://github.com/itsBabuaa)
⭐ If you found this project helpful, please consider giving it a star!
