from copyreg import pickle
from flask import Flask, request
import streamlit as st
import pickle
from sklearn.linear_model import LogisticRegression

pickled_model_file = open("pickle_wine_model.pkl", "rb")
classifier = pickle.load(pickled_model_file)

def predict_wine():

    try :
        st.title("Model Deployment")
        p1 = st.text_input("Predictor1")
        p2 = st.text_input("Predictor2")
        p3 = st.text_input("Predictor3")
        p4 = st.text_input("Predictor4")
        p5 = st.text_input("Predictor5")
        p6 = st.text_input("Predictor6")
        p7 = st.text_input("Predictor7")
        p8 = st.text_input("Predictor8")
        p9 = st.text_input("Predictor9")
        p10 = st.text_input("Predictor10")
        p11 = st.text_input("Predictor11")
        p12 = st.text_input("Predictor12")
        p13 = st.text_input("Predictor13")

        result = classifier.predict([[p1,p2,p3,p4,p5,p6,p7,p8,p9,p10,p11,p12,p13]])
        
        if st.button("Print output"):
            st.success(result)
    except Exception as e :
        return f" Error occuredd with message : {e}"

if __name__=="__main__":
    predict_wine()