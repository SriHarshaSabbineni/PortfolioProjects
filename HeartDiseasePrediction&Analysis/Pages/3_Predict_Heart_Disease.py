import streamlit as st
import numpy as np
import pickle
loaded_model = pickle.load(open('trained_model.sav','rb'))
def heart_dis_prediction(input_data):

    input_data_as_np_array = np.array(input_data, dtype=float)
    reshaped_data = input_data_as_np_array.reshape(1, -1)
    prediction = loaded_model.predict(reshaped_data)
    if (prediction[0]==0):
        return "The person does not have heart disease"
    else:
        return "The person has heart disease"

three, four = st.columns([2, 10])
three.image("heart_img4.jpg", width=100, clamp=True)
four.header('Heart Disease Prediction')
st.write("Enter patient details to predict heart disease:")

ph1 = st.empty()
age = ph1.text_input('age')
ph2 = st.empty()
sex = ph2.text_input('sex: male=1 female=0')
ph3 = st.empty()
cp = ph3.text_input('chest pain type: 0/1/2/3')
ph4 = st.empty()
trestbps = ph4.text_input('resting blood pressure (in mm Hg on admission to the hospital)')
ph5 = st.empty()
chol = ph5.text_input('serum cholesterol in mg/dl')
ph6 = st.empty()
fbs = ph6.text_input('fasting blood sugar > 120 mg/dl (1 = true; 0 = false)')
ph7 = st.empty()
restecg = ph7.text_input('resting electrocardiographic results: 0/1/2')
ph8 = st.empty()
thalach = ph8.text_input('maximum heart rate achieved')
ph9 = st.empty()
exang = ph9.text_input('exercise induced angina (1 = yes; 0 = no)')
ph10 = st.empty()
oldpeak = ph10.text_input('ST depression induced by exercise relative to rest')
ph11 = st.empty()
slope = ph11.text_input('the slope of the peak exercise ST segment')
ph12 = st.empty()
ca = ph12.text_input('number of major vessels (0-3) colored by flourosopy')
ph13 = st.empty()
thal = ph13.text_input('1 = normal; 2 = fixed defect; 3 = reversable defect')

five, six = st.columns([3, 7])
click_clear = five.button('Check for another Patient', key=1)

if click_clear:
    age = ph1.text_input('age', key=2)
    sex = ph2.text_input('sex: male=1 female=0', key=3)
    cp = ph3.text_input('chest pain type: 0/1/2/3', key=4)
    trestbps = ph4.text_input('resting blood pressure (in mm Hg on admission to the hospital)', key=5)
    chol = ph5.text_input('serum cholesterol in mg/dl', key=6)
    fbs = ph6.text_input('fasting blood sugar > 120 mg/dl (1 = true; 0 = false)', key=7)
    restecg = ph7.text_input('resting electrocardiographic results: 0/1/2', key=8)
    thalach = ph8.text_input('maximum heart rate achieved', key=9)
    exang = ph9.text_input('exercise induced angina (1 = yes; 0 = no)', key=10)
    oldpeak = ph10.text_input('ST depression induced by exercise relative to rest', key=11)
    slope = ph11.text_input('the slope of the peak exercise ST segment', key=12)
    ca = ph12.text_input('number of major vessels (0-3) colored by flourosopy', key=13)
    thal = ph13.text_input('1 = normal; 2 = fixed defect; 3 = reversable defect', key=14)

diagnosis = ''

if six.button('Predict'):
    diagnosis = heart_dis_prediction([age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal])

st.success(diagnosis)