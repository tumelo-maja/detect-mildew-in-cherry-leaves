import streamlit as st
from app_pages.multipage import MultiPage

st.set_page_config(
    page_title="Powdery Mildew Detector",
    page_icon="🍒",
    layout="wide"
)

# Load CSS
def load_styles(file_path):
    with open(file_path) as f:
        st.html(f"<style>{f.read()}</style>")


load_styles("app_pages/style.css")

st.html(
    """
    <div class='head-wrap'>
        <h1 class='head-title'>🍃 Powdery Mildew Detector</h1>
        <p class='head-title'>A visual diagnosis and ML prediction dashboard for cherry leaf disease</p>
    </div>
    """
)

# load pages scripts
from app_pages.page_summary import page_summary_body
from app_pages.page_leaf_visualiser import page_leaf_visualiser_body
from app_pages.page_powdery_mildew_detector import page_powdery_mildew_detector_body
from app_pages.page_project_hypothesis import page_project_hypothesis_body
from app_pages.page_ml_performance import page_ml_performance_diagnostics

app = MultiPage(app_name="Powdery Mildew Detector")  # Create an instance of the app

# Add your app pages here using .add_page()
app.add_page("Quick Project Summary", page_summary_body)
app.add_page("Project Hypothesis", page_project_hypothesis_body)
app.add_page("Leaf Visualiser", page_leaf_visualiser_body)
app.add_page("Powdery Mildew detector", page_powdery_mildew_detector_body)
app.add_page("ML Performance Diagnostics", page_ml_performance_diagnostics)

app.run()  # Run the app