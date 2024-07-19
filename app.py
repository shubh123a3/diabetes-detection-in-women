import  streamlit as st
import pickle

import pandas as pd
model=pickle.load(open('model.pkl','rb'))
st.title('Diabetes Prediction')
st.write('This app predicts the probability of a person having diabetes based on the data' )
col1,col2=st.columns(2)
pregnancies=col1.number_input('Enter the number of pregnancies',min_value=0, max_value=17, value=0)
glucose=col2.number_input('Enter the glucose level',min_value=0, max_value=200, value=0)
col3,col4=st.columns(2)
bmi=col3.number_input('Enter the BMI',min_value=0, max_value=70, value=0)
age=col4.number_input('Enter the age',min_value=0, max_value=100, value=0)
if st.button('Predict'):

    input_df=pd.DataFrame({
            'Pregnancies':[pregnancies],
            'Glucose':[glucose],
            'BMI':[bmi],
            'Age':[age]
         })
    result=model.predict(input_df)
    if result[0]==0:
        st.write('You do not have diabetes')
    else:
        st.write('You have diabetes')
# Path: requirements.txt
# streamlit==1.0.0
# pandas==1.3.3
# numpy==1.21.2
# joblib==1.0.1


