import streamlit as st
import tensorflow as tf
from tensorflow.keras.models import load_model
from sklearn.preprocessing import StandardScaler, LabelEncoder, OneHotEncoder
import pandas as pd
import pickle

# Loading trained model
model= load_model('model.h5')

# load the encoder and scaler
le_gender= pickle.load(open('le_gender.pkl', 'rb'))
ohe_geo= pickle.load(open('ohe_geo.pkl', 'rb'))
sc= pickle.load(open('sc.pkl', 'rb'))

# Streamlit UI

st.set_page_config(page_title="Customer Churn Predictor", page_icon="📋", layout="centered")

st.title("📋 Crustomer Churn Predictor")
#st.markdown("### Welcome to your Crustomer Churn Predictor!")

col1, col2 = st.columns(2)
with col1:
    Geography= st.selectbox('Geography', ohe_geo.categories_[0])
with col2:
    Gender= st.selectbox('Gender', le_gender.classes_)


col3, col4, col5= st.columns(3)
with col3:
    Age= st.slider('Age', 18, 92)
with col4:
    Tenure= st.slider('Tenure', 0, 10)
with col5:
    NumOfProducts= st.slider('Num Of Products', 1, 4)


col6, col7, col8= st.columns(3)
with col6:
    Balance= st.number_input('Balance')
with col7:
    CreditScore= st.number_input('Credit Score')
with col8:
    EstimatedSalary= st.number_input('Estimated Salary')


col9, col10 = st.columns(2)
with col9:
    HasCrCard= st.selectbox('Has Credit Card', [0, 1])
with col10:
    IsActiveMember= st.selectbox('Is Active Member', [0, 1])


input_data= pd.DataFrame({
    'CreditScore': [CreditScore],
    'Gender': [le_gender.transform([Gender])[0]],
    'Age': [Age],
    'Tenure': [Tenure],
    'Balance': [Balance],
    'NumOfProducts': [NumOfProducts],
    'HasCrCard': [HasCrCard],
    'IsActiveMember': [IsActiveMember],
    'EstimatedSalary': [EstimatedSalary]
})

# Encoding Geography data
geo_encoder= ohe_geo.transform([[Geography]])
geo_encoded_df= pd.DataFrame(geo_encoder, columns= ohe_geo.get_feature_names_out())

input_data= pd.concat([geo_encoded_df, input_data.reset_index(drop= True)], axis= 1)

# Scale the input data
input_scaled= sc.transform(input_data)


# Prediction
if st.button('Predict'):

    prediction= model.predict(input_scaled)
    prediction_proba= prediction[0][0]
    
    st.header(f'Churn Probability: {round(prediction_proba *100)}%')

    if prediction_proba > 0.5:
        st.header('The customer is likely to churn!')
    else:    
        st.header('The customer is not likely to churn!')


st.markdown(
    """
    <style>
        .footer {
            position: fixed;
            left: 0;
            bottom: 5px;
            width: 100%;
            text-align: center;
            font-size: 13px;
            opacity: 0.4;
        }
    </style>
    <div class="footer">
        Babuaa ;)
    </div>
    """,
    unsafe_allow_html=True
)
