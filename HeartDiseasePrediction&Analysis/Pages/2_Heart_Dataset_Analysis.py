import streamlit as st
import pandas as pd

one, two = st.columns([2, 10])
one.image("heart_img5.jpg", width=100, clamp=True)
two.header('Heart Disease Data Analysis')
st.markdown("<hr>", unsafe_allow_html=True)

st.write("Here are the top few rows from the dataset:")
heart_data = pd.read_csv('C:/Users/navee/PycharmProjects/mlpython/heart.csv')
st.table(heart_data.head())
st.write("Here is the description for each column in the dataset:")

data = {
    'Attribute': ['Age', 'Sex', 'ChestPain(cp)', 'Resting Blood Pressure(trestbps)', 'Serum Cholesterol(chol)',
                  'Fasting Blood Sugar > 120 mg/dl (fbs)',
                  'Resting ECG(restecg)', 'Max Heart Rate(thalach)', 'Exercise Angina(exang)', 'Oldpeak', 'ST Slope(slope)', 'CA', 'Thal', 'Heart Disease(target)'],
    'Description': ['Age of a patient [years]', 'Gender of the patient [M: Male, F: Female]',
                    'Chest pain type [1: Typical Angina, 2: Atypical Angina, 3: Non-Anginal Pain, 0: Asymptomatic]',
                    'Blood pressure in Hg (Normal blood pressure - 120/80 Hg)',
                    'Serum cholesterol level in blood (Normal cholesterol level below for adults 200mg/dL)',
                    'True or False',
                    'Resting electrocardiogram results [0: Normal, 1: having ST-T wave abnormality '
                    '(T wave inversions and/or ST elevation or depression of > 0.05 mV), '
                    '2: showing probable or definite left ventricular hypertrophy by Estes\' criteria]',
                    'Maximum heart rate achieved [Numeric value between 60 and 202]',
                    'Exercise-induced angina [Y: Yes, N: No]',
                    'ST [Numeric value measured in depression]',
                    'The slope of the peak exercise ST segment [Up(0): upsloping, Flat(1): flat, Down(2): downsloping]',
                    'Number of major vessels (0-3) colored by fluoroscopy',
                    '0 = normal; 1 = fixed defect; 2 = reversible defect',
                    'Output class [1: heart disease, 0: Normal]']
}
df = pd.DataFrame(data)
st.table(df)
st.markdown("<hr>", unsafe_allow_html=True)
st.write("Here is the Correlation Matrix displayed as a heat map which shows how the above variables are correlated to each other:")
st.image("heart_dataset_correlation_matrix.png")
st.write("From the above correlation matrix, we can see that there is highest correlation between heart disease and Chest Pain Type(cp), Maximum Heart Rate(thalach), and ST Slope(slope)")
st.markdown("<hr>", unsafe_allow_html=True)
st.write("This pie chart shows the distribution of Heart Diseases among Men and Women:")
st.image("da1.png")
st.write("From the above chart we can see that more percentage of women are imacted by heart disease compared to men.")
st.markdown("<hr>", unsafe_allow_html=True)
st.image("da2.png")
st.write("From the above clustered column chart we can see that, most patients who are asymptomatic(without any chest pain) do not have heart disease.")
st.write("Atypical Angina is the leading symptom of presence of heart disease.")
st.markdown("<hr>", unsafe_allow_html=True)
st.image("da3.png")
st.write("From the above area chart we can see that patients with heart disease have their maximum heart rate on the higher end.")
st.markdown("<hr>", unsafe_allow_html=True)
st.image("da4.png")
st.write("From the above clustered column chart we can see that, slop of 2 i.e. Downsloping in ST Slope is a symptom of presence of heart disease.")
st.markdown("<hr>", unsafe_allow_html=True)