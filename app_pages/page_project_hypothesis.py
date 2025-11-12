import streamlit as st
import matplotlib.pyplot as plt

def page_project_hypothesis_body():
    st.write("## Project Hypotheses")
    st.write(f"Details of the project's hypothesis and validations are presented below.")
    
    st.write("#### Hypothesis 1")
    st.success("* Leaves infected by powdery mildew have visual markers that make them distinguishable from healthy leaves.")
    st.info(
        "Infected leaves typically develop a light-green circular lesion, followed by a white, powder-like growth. "
        "Healthy leaves do not show these patterns."
    )
    st.write("---")

    st.write("### Hypothesis 2")
    st.success("* A convolutional neural network (CNN) can learn to detect powdery mildew from leaf images.")
    st.info(
        "The model was trained to identify visual patterns/markers linked to the powdery mildew infection. "
        "During training, the model improved its ability to differentiate healthy and infected leaves."
    )
    st.write(
        "See the **ML Performance** page to review loss, accuracy, confusion matrix and ROC curve."
    )   