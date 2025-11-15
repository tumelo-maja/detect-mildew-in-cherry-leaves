import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from src.machine_learning.evaluate_clf import load_test_evaluation

def page_ml_performance_diagnostics(version="v1"):
    st.write("## Machine Learning Diagnostics")
    st.info(f"This page presents dataset distribution, machine learning setup,"
            " model performance and evaluation with unseen data.")

    st.write("### Train, Validation and Test Set: Labels Frequencies")
    dist_img = plt.imread(f"outputs/{version}/bar_freq_label_distribution.png")
    st.image(dist_img, caption="Images per dataset split (Train / Validation / Test)")

    pie_img = plt.imread(f"outputs/{version}/pie_set_distribution.png")
    st.image(pie_img, caption="Dataset percentage distribution")

    st.write(
        "The dataset was divided into training, validation, and testing subsets. "
        "The training set teaches the model, the validation set helps tune it, "
        "and the test set evaluates final performance."
    )
    st.write("---")

    st.write("### Model Performance Metrics")
    clf_img = plt.imread(f"outputs/{version}/classification_report.png")
    st.image(clf_img, caption="Classification Report")

    st.write(
        "The classification report shows Precision, Recall, and F1 Score. "
        "Higher values indicate better performance. "
        "The model shows strong ability to distinguish healthy leaves from infected leaves."
    )
    st.write("---")

    st.write("### ROC Curve and Confusion Matrix")
    roc_img = plt.imread(f"outputs/{version}/roc_auc_curve.png")
    st.image(roc_img, caption="ROC Curve")

    cm_img = plt.imread(f"outputs/{version}/confusion_matrix.png")
    st.image(cm_img, caption="Confusion Matrix")

    st.write(
        "The ROC curve indicates how well the model separates the two classes. "
        "The confusion matrix shows where the model makes correct and incorrect predictions."
    )
    st.write("---")

    st.write("### Training Progress Over Time")
    perf_img = plt.imread(f"outputs/{version}/model_training_loss_accuracy.png")
    st.image(perf_img, caption="Training vs Validation Loss and Accuracy")

    st.write(
        "A smooth training curve with similar training and validation performance "
        "suggests the model learned general patterns rather than memorizing the dataset."
    )
    st.write("---")

    st.write("### Final Model Evaluation on Test Set")
    results = pd.DataFrame(load_test_evaluation(version), index=["Loss", "Accuracy"])
    results.columns = ["Value"]
    st.dataframe(results.style.format("{:.4f}"))

    st.write(
        "These results show how the model performs on completely new images that were not part of training."
    )