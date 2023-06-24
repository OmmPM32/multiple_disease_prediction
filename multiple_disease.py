# -*- coding: utf-8 -*-
"""
Created on Tue Apr 25 10:32:39 2023

@author: ommpr
"""
import numpy as np
import pickle
import streamlit as st
from streamlit_option_menu import option_menu 
 
# loading the saved models
diabetes_model = pickle.load(open('D:/Major Project/Multiple Disease Prediction/models/diabetes_model.sav', 'rb'))

Heart_Disease_model = pickle.load(open('D:/Major Project/Multiple Disease Prediction/models/Heart_Disease_model.sav','rb'))

Parkinsons_model = pickle.load(open('D:/Major Project/Multiple Disease Prediction/models/parkinsons_model.sav','rb'))

Breast_cancer_model = pickle.load(open('D:/Major Project/Multiple Disease Prediction/models/Breast_cancer_model.sav','rb'))

# sidebar/navigation

with st.sidebar:
    selected = option_menu('Multiple Disease Prediction System',
                           ['Diabetes Prediction',
                            'Heart Disease Prediction',
                            'Parkinsons Disease Prediction',
                            'Breast cancer Prediction'],
                           icons = ['align-bottom','activity','person',''],
                           default_index = 0)
    
# Diabetes Prediction Page
if (selected == 'Diabetes Prediction'):
    
    # page title
    st.title('Diabetes Prediction using ML')
    
    
    # getting the input data from the user
    col1, col2, col3 = st.columns(3)
    
    with col1:
        Pregnancies = st.text_input('Number of Pregnancies')
        
    with col2:
        Glucose = st.text_input('Glucose Level')
    
    with col3:
        BloodPressure = st.text_input('Blood Pressure value')
    
    with col1:
        SkinThickness = st.text_input('Skin Thickness value')
    
    with col2:
        Insulin = st.text_input('Insulin Level')
    
    with col3:
        BMI = st.text_input('BMI value')
    
    with col1:
        DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree Function value')
        
    with col2:
        Age = st.text_input('Age of the Person')
    
    
    # code for Prediction
    diab_diagnosis = ''
    
    # creating a button for Prediction    
    if st.button('Diabetes Test Result'):
        diab_prediction = diabetes_model.predict([[Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]])
        
        if (diab_prediction[0] == 1):
          diab_diagnosis = 'The person is diabetic'
        else:
          diab_diagnosis = 'The person is not diabetic'
        
    st.success(diab_diagnosis)




# Heart Disease Prediction Page
if (selected == 'Heart Disease Prediction'):
    
    # page title
    st.title('Heart Disease Prediction using ML')
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        age = st.text_input('Age')
        
    with col2:
        sex = st.text_input('Sex')
        
    with col3:
        cp = st.text_input('Chest Pain types')
        
    with col1:
        trestbps = st.text_input('Resting Blood Pressure')
        
    with col2:
        chol = st.text_input('Serum Cholestoral in mg/dl')
        
    with col3:
        fbs = st.text_input('Fasting Blood Sugar > 120 mg/dl')
        
    with col1:
        restecg = st.text_input('Resting Electrocardiographic results')
        
    with col2:
        thalach = st.text_input('Maximum Heart Rate achieved')
        
    with col3:
        exang = st.text_input('Exercise Induced Angina')
        
    with col1:
        oldpeak = st.text_input('ST depression induced by exercise')
        
    with col2:
        slope = st.text_input('Slope of the peak exercise ST segment')
        
    with col3:
        ca = st.text_input('Major vessels colored by flourosopy')
        
    with col1:
        thal = st.text_input('thal: 0 = normal; 1 = fixed defect; 2 = reversable defect')
        
     
    # code for Prediction
    heart_diagnosis = ''
    
    # creating a button for Prediction
    
    if st.button('Heart Disease Test Result'):
        a = np.array([age, sex, cp, trestbps, chol, fbs, restecg,thalach,exang,oldpeak,slope,ca,thal])
        numeric_array = a.astype(float)
        heart_prediction = Heart_Disease_model.predict([numeric_array])                          
        print(heart_prediction)
        if (int(heart_prediction[0]) == 1):
          heart_diagnosis = 'The person is having heart disease'
        else:
          heart_diagnosis = 'The person does not have any heart disease'
        
    st.success(heart_diagnosis)
        
    
    

# Parkinson's Prediction Page
if (selected == "Parkinsons Disease Prediction"):
    
    # page title
    st.title("Parkinson's Disease Prediction using ML")
    
    col1, col2, col3, col4, col5 = st.columns(5)  
    
    with col1:
        fo = st.text_input('Fo(Hz)')
        
    with col2:
        fhi = st.text_input('Fhi(Hz)')
        
    with col3:
        flo = st.text_input('Flo(Hz)')
        
    with col4:
        Jitter_percent = st.text_input('Jitter(%)')
        
    with col5:
        Jitter_Abs = st.text_input('Jitter(Abs)')
        
    with col1:
        RAP = st.text_input('RAP')
        
    with col2:
        PPQ = st.text_input('PPQ')
        
    with col3:
        DDP = st.text_input('DDP')
        
    with col4:
        Shimmer = st.text_input('Shimmer')
        
    with col5:
        Shimmer_dB = st.text_input('Shimmer(dB)')
        
    with col1:
        APQ3 = st.text_input('APQ3')
        
    with col2:
        APQ5 = st.text_input('APQ5')
        
    with col3:
        APQ = st.text_input('APQ')
        
    with col4:
        DDA = st.text_input('DDA')
        
    with col5:
        NHR = st.text_input('NHR')
        
    with col1:
        HNR = st.text_input('HNR')
        
    with col2:
        RPDE = st.text_input('RPDE')
        
    with col3:
        DFA = st.text_input('DFA')
        
    with col4:
        spread1 = st.text_input('spread1')
        
    with col5:
        spread2 = st.text_input('spread2')
        
    with col1:
        D2 = st.text_input('D2')
        
    with col2:
        PPE = st.text_input('PPE')
        
    
    
    # code for Prediction
    parkinsons_diagnosis = ''
    
    # creating a button for Prediction     
    if st.button("Parkinson's Test Result"):
        parkinsons_prediction = Parkinsons_model.predict([[fo, fhi, flo, Jitter_percent, Jitter_Abs, RAP, PPQ,DDP,Shimmer,Shimmer_dB,APQ3,APQ5,APQ,DDA,NHR,HNR,RPDE,DFA,spread1,spread2,D2,PPE]])                          
        
        if (parkinsons_prediction[0] == 1):
          parkinsons_diagnosis = "The person has Parkinson's disease"
        else:
          parkinsons_diagnosis = "The person does not have Parkinson's disease"
        
    st.success(parkinsons_diagnosis)


# Breast cancer Prediction Page
if (selected == 'Breast cancer Prediction'):
    
    # page title
    st.title('Breast cancer Prediction using ML')
    
    
    # getting the input data from the user
    col1, col2, col3, col4, col5 = st.columns(5)
    
    with col1:
        radius_mean = st.text_input('Radius Mean')
        
    with col2:  
        Texture_mean = st.text_input('Texture Mean')
    
    with col3:
        Perimeter_mean = st.text_input('Perimeter Mean')
    
    with col4:
        Area_mean = st.text_input('Area Mean')
    
    with col5:
        smoothness_mean = st.text_input('Smoothness Mean')
    
    with col1:
        compactness_mean = st.text_input('Compactness Mean')
    
    with col2:
        concavity_mean = st.text_input('Concavity Mean')
    
    with col3:
        concavePoints_mean = st.text_input('Concave Points mean')
        
    with col4:
        symmetry_mean = st.text_input('Symmetry Mean')
        
    with col5:
        FD_mean = st.text_input('FD Mean')
        
    with col1:
        radius_se = st.text_input('Radius Se')
        
    with col2:
        texture_se = st.text_input('Texture Se')
    
    with col3:
        perimeter_se = st.text_input('Perimeter Se')
        
    with col4:
        area_se = st.text_input('Area Se')
        
    with col5:
        smoothness_se = st.text_input('Smoothness Se')
        
    with col1:
        compactness_se = st.text_input('compactness_se')
        
    with col2:
        concavity_se = st.text_input('concavity_se')
    
    with col3:
        concavePoints_se = st.text_input('concave points_se')
    
    with col4:
        symmetry_se = st.text_input('Symmetry se')    
        
    with col5:
        fractal_dimension_se = st.text_input('FD Se')
        
    with col1:
        radius_worst = st.text_input('radius worst')
        
    with col2:
        texture_worst = st.text_input('texture worst')
        
    with col3:
        perimeter_worst = st.text_input('perimeter worst')
    
    with col4:
        area_worst = st.text_input('area worst')
        
    with col5:
        smoothness_worst = st.text_input('smoothness_worst')
        
    with col1:
        compactness_worst = st.text_input('compactness_worst') 
        
    with col2:
        concavity_worst = st.text_input('Concavity Worst')
        
    with col3:
        concavepoints_worst = st.text_input('concave points worst')
    
    with col4:
        symmetry_worst = st.text_input('Symmetry worst')
        
    with col5:
        fractal_dimension_worst = st.text_input('FD worst')
            
    
    # code for Prediction
    BC_diagnosis = ''
    
    # creating a button for Prediction
    
    if st.button('Breast Cancer Test Result'):
        b = np.array([radius_mean, Texture_mean, Perimeter_mean, Area_mean, smoothness_mean, compactness_mean, concavity_mean, concavePoints_mean, symmetry_mean, FD_mean, radius_se, texture_se, perimeter_se, area_se, smoothness_se, compactness_se, concavity_se, concavePoints_se, symmetry_se, fractal_dimension_se, radius_worst, texture_worst, perimeter_worst, area_worst, smoothness_worst, compactness_worst, concavity_worst, concavepoints_worst, symmetry_worst, fractal_dimension_worst])
        c = b.astype(float)
        BC_prediction = Breast_cancer_model.predict([c])
        if (BC_prediction[0] == 1):
          BC_diagnosis = 'The cancer is Benign'
        else:
          BC_diagnosis = 'The cancer is Malignant'
        
    st.success(BC_diagnosis)
    