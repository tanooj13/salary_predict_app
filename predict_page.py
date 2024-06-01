import streamlit as st
import pickle as pk
import numpy as np



def load_model():
    with open('sal_predict','rb') as file:
        model = pk.load(file)
    return model

model = load_model()

def info():
    exp = st.slider("Experience:",0,100,key = "exp")

    test_score = st.number_input("Test Score",0,10,key = "test_score")

    int_score = st.number_input("Interview Score",0,10,key = "int_score")

    return [[exp,test_score,int_score]]

def cal_sal(values):
    pred_button = st.button("Calculate Salary")
    sal = 0
    if pred_button:
        sal = model.predict(values)
        st.subheader("Your Estimated Salary in ($):")
        st.write(sal)
    
def show_predict_page():
    st.title('Software Developer Salary Prediction')

    st.write("""### We need some Info to predict the salary""")
    val = info()
    cal_sal(val)



