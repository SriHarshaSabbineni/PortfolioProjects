import numpy as np
import pickle
import streamlit as st

loaded_model = pickle.load(open('trained_model.sav','rb'))

def heart_dis_prediction(input_data):

    input_data_as_np_array = np.array(input_data, dtype=float)
    reshaped_data = input_data_as_np_array.reshape(1, -1)
    prediction = loaded_model.predict(reshaped_data)
    if (prediction[0]==0):
        return "The person does not have heart disease"
    else:
        return "The person has heart disease"

def main():
    st.title("Heart Disease Prediction")
    age = st.text_input('age')
    sex = st.text_input('sex: male=1 female=0')
    cp = st.text_input('chest pain type: 0/1/2/3')
    trestbps = st.text_input('resting blood pressure (in mm Hg on admission to the hospital)')
    chol = st.text_input('serum cholesterol in mg/dl')
    fbs = st.text_input('fasting blood sugar > 120 mg/dl (1 = true; 0 = false)')
    restecg = st.text_input('resting electrocardiographic results: 0/1/2')
    thalach = st.text_input('maximum heart rate achieved')
    exang = st.text_input('exercise induced angina (1 = yes; 0 = no)')
    oldpeak = st.text_input('ST depression induced by exercise relative to rest')
    slope = st.text_input('the slope of the peak exercise ST segment')
    ca = st.text_input('number of major vessels (0-3) colored by flourosopy')
    thal = st.text_input('1 = normal; 2 = fixed defect; 3 = reversable defect')

    diagnosis = ''

    if st.button('Predict'):
        diagnosis = heart_dis_prediction([age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal])

    st.success(diagnosis)

if __name__ == '__main__':
    main()