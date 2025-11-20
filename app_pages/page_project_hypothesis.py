import streamlit as st
import matplotlib.pyplot as plt


def page_project_hypothesis_body(version="v1"):
    st.write("## Project Hypotheses")
    st.write(
        "Details of the project's hypothesis "
        "and validations are presented below.")

    st.write("#### Hypothesis 1")
    st.success(
        "* Leaves infected by powdery mildew have "
        "visual markers that make them distinguishable from healthy leaves.")
    st.info(
        "Infected leaves typically develop a light-green circular lesion, "
        "followed by a white, powder-like growth. "
        "Healthy leaves do not show these patterns.\n\n"
        "**Validation:**\n\n"
        "- Generate and inspect average and variability images for healthy and infected leaves."
    )
    st.write("---")

    st.write("### Hypothesis 2")
    st.success(
        "* A convolutional neural network (CNN) "
        "can learn to detect powdery mildew from leaf images.")
    st.info(
        "The model was trained to identify visual patterns/markers "
        "linked to the powdery mildew infection. "
        "During training, the model improved its ability "
        "to differentiate healthy and infected leaves.\n\n"
        "**Validation:**\n"
        "- Apply image augmentation to create additional variations of the leaf images and improve the model's generalization of powdery mildew patterns/markers.\n"
        "- Train a classification CNN model\n"
        "- Evaluate model performance against the project's success metrics\n"
        "- If the model underperforms, re-train by adjusting CNN layer structure or configuration.\n"
        "- Test the model on unseen images."
    )

    st.write("### Hypothesis 3")
    st.success(
        "* Image background or other objects in the image does not "
        "have any effect on the model's performance.")
    st.info(
        "The model was trained using images with a controlled background and "
        "each image contained only 1 leaf. "
        "In a practical application of this ML solution, images may "
        "contain more than 1 leaf since the picture will likely be taken "
        "while all leaves are attached to the plant. "
        "When tested with a multi-leaf image, "
        "the mode's predictions performed poorly.\n\n"
        "**Validation:**\n"
        "- Use an image with other objects, lightings "
        "and or multiple leave to test if an accurate prediction is given."
    )    
    st.write(
        "See the **ML Performance** page to "
        "review loss, accuracy, confusion matrix and ROC curve."
    )
