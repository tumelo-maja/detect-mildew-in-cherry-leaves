import streamlit as st
import matplotlib.pyplot as plt


def page_summary_body(version="v1"):

    st.write("### Project Summary")

    st.info(
        "**General Information**\n\n"
        "Powdery mildew is a fungal disease that commonly affects cherry leaves."
        " It usually begins as small pale spots that slowly spread across the leaf surface."
        " As the infection grows, the leaf develops a white, powder-like coating."
        " Powdery mildew often spreads quickly across young leaves and new growth, making it harder for the plant to stay healthy.\n\n"

        "In this project, images of both healthy leaves and leaves with powdery mildew were collected so the model could learn to tell the difference.\n\n"        "Infected leaves often show noticeable visual changes, such as:\n"
        "* Small pale circular spots appearing on the surface of the leaf.\n"
        "* A thin white, powder-like coating that spreads across one or both sides of the leaf.\n"
        "* Leaves may become dull or lose their normal healthy texture as the infection grows.\n\n"
        )

    st.warning(
        "**Project Dataset**\n\n"
        "The available dataset contains:\n"
        "* 2104 images of healthy leaves\n"
        "* 2104 images of leaves infected by powdery mildew\n\n"
        "Dataset source: [Kaggle - Code Institute Cherry Leaves Dataset](https://www.kaggle.com/datasets/codeinstitute/cherry-leaves)"
        )
    st.write("---")

    st.write("### Business Requirements")
    st.success(
        "1. **Visual comparison** between healthy and infected leaves.\n\n"
        "2. **Model-based prediction** to determine if a given leaf is infected by powdery mildew or not.\n\n"
        "3. **Downloadable report** summarizing predictions for uploaded images.\n\n")
    st.write("---")         

    st.write(
        "**More details:**\n"
        "For additional information about the project and findings, see "
        "[README](https://github.com/tumelo-maja/detect-mildew-in-cherry-leaves#readme).")