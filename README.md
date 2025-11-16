# Powdery Mildew Detector

<figure>
  <img src="docs/readme_images/application-mock.png" width="600px" >
  <br>
  <figcaption><strong><em>Application Mockup: Powdery Mildew Detector</em></strong></figcaption>
</figure>

[Link to Dashboard on Streamlit](https://detect-mildew-in-cherry-leaves-2zq3hwsa6w44mqxdq9d9vd.streamlit.app/)

## Table of Contents

- [Powdery Mildew Detector](#powdery-mildew-detector)
  - [Table of Contents](#table-of-contents)
  - [Project Summary](#project-summary)
  - [Dataset Content](#dataset-content)
  - [Business Requirements](#business-requirements)
  - [Hypotheses and validations](#hypotheses-and-validations)
    - [**Hypothesis 1**](#hypothesis-1)
    - [**Hypothesis 2**](#hypothesis-2)
  - [The rationale to map the business requirements to the Data Visualisations and ML tasks](#the-rationale-to-map-the-business-requirements-to-the-data-visualisations-and-ml-tasks)
    - [**Business Requirement 1: Visual Understanding of Leaf Conditions**](#business-requirement-1-visual-understanding-of-leaf-conditions)
    - [**Business Requirement 2: Classification and Prediction**](#business-requirement-2-classification-and-prediction)
  - [ML Business Case](#ml-business-case)
  - [Dashboard Design](#dashboard-design)
    - [Page 1: Project Summary](#page-1-project-summary)
    - [Page 2: Leaf Visualizer](#page-2-leaf-visualizer)
    - [Page 3: Mildew Detector](#page-3-mildew-detector)
    - [Page 4: Project Hypotheses and Validation](#page-4-project-hypotheses-and-validation)
    - [Page 5: ML Performance Metrics](#page-5-ml-performance-metrics)
  - [User stories and Testing](#user-stories-and-testing)
  - [Code validation](#code-validation)
  - [Bugs](#bugs)
  - [Deployment](#deployment)
    - [Heroku - NOT USED](#heroku---not-used)
    - [Streamlit](#streamlit)
  - [Main Data Analysis and Machine Learning Libraries](#main-data-analysis-and-machine-learning-libraries)
  - [Other Technologies Used](#other-technologies-used)
  - [Limitations and Considerations](#limitations-and-considerations)
  - [Credits](#credits)
  - [Acknowledgements](#acknowledgements)

## Project Summary

The cherry plantation crop from Farmy & Foods is facing a challenge where their cherry plantations have been presenting powdery mildew. Currently, the process is manual verification if a given cherry tree contains powdery mildew. An employee spends around 30 minutes in each tree, taking a few samples of tree leaves and verifying visually if the leaf tree is healthy or has powdery mildew. If there is powdery mildew, the employee applies a specific compound to kill the fungus. The time spent applying this compound is 1 minute. The company has thousands of cherry trees located on multiple farms across the country. As a result, this manual process is not scalable due to the time spent in the manual process inspection.

To save time in this process, the IT team suggested an ML system that detects instantly, using a leaf tree image, if it is healthy or has powdery mildew. A similar manual process is in place for other crops for detecting pests, and if this initiative is successful, there is a realistic chance to replicate this project for all other crops. The dataset is a collection of cherry leaf images provided by Farmy & Foods, taken from their crops.

## Dataset Content

The dataset is sourced from [Kaggle - Code Institute, Cherry-leaves](https://www.kaggle.com/codeinstitute/cherry-leaves). The dataset contains +4 thousand images taken from the client's crop fields. The images show healthy cherry leaves and cherry leaves that have powdery mildew, a fungal disease that affects many plant species. The cherry plantation crop is one of the finest products in their portfolio, and the company is concerned about supplying the market with a compromised quality product.

The dataset contains **4,208** labeled images of cherry leaves:

- **2,104 Healthy**
- **2,104 Infected with powdery mildew**

All images were captured under similar conditions, with individual leaves photographed against a uniform background to reduce noise and focus on visible symptoms.

## Business Requirements

The goal is to create a machine learning model that detects powdery mildew on leaves from images.

1. **Visual Assessment:** Study and understand visual differences between healthy and infected leaves.
2. **Model Prediction:** Develop a model-based approach to classify leaf images as healthy or infected.
3. **User Interaction:** Provide an interface allowing users to submit and analyse one or more leaf images and receive classification predictions with an option to download a report.

## Hypotheses and validations

This section outlines the main assumptions that guided the development of the project and explains how each was tested and evaluated.

### **Hypothesis 1**

There are clear visual markers/characteristic in leaves that differentiate healthy leaves from those infected by powdery mildew fungus.

**Approach:** Generate and inspect average and variability images for healthy and infected leaves.

### **Hypothesis 2**

A Convolutional Neural Network (CNN) model can be trained to recognize distinctive visual features to accurately classify leaves as healthy or infected.

**Approach:**

- **Image augmentation techniques:** to create additional variations of the leaf image to improve the model's learning of general visual patterns.
- Train a classification CNN model
- Evaluate model performance against the project's success metrics
- Test the model on unseen images.

## The rationale to map the business requirements to the Data Visualisations and ML tasks

The project has two main goals: first, to understand how powdery mildew visually affects cherry leaves, and second, to build a reliable model that can detect the infection from images.

### **Business Requirement 1: Visual Understanding of Leaf Conditions**

To explore whether infected leaves show consistent visual patterns, the dashboard includes several image-based visualizations:

- **Average and variability images** for healthy and infected leaves help to highlight visual differences.
- A **difference image** between average healthy and infected leaves is shown to examine whether there are visible high-level distinctions.
- An **image montage** allows users to view random image examples of infected or healthy leaves.

### **Business Requirement 2: Classification and Prediction**

- A **binary image classifier** is trained to distinguish between *healthy* and *infected* leaves.
- Users can **upload their own leaf images** and gte live predictions.
- A **summary table** of predictions is generated and can be **downloaded** as csv.

## ML Business Case

- Develop an ML model to predict whether a leaf is infected with powdery mildew or not. The model is supervised, with two classes and a single-label classification.
- The ideal outcome is to provide the client with an efficient and reliable tool for mildew detection, allowing earlier treatment and reducing crop loss.  
- **Model success metrics:**  
  - Achieve accuracy of 97% or above on the test set.  
- **Model output:** a flag indicating whether the leaf is infected with mildew or not, along with the associated probability. The client can upload one or more images with leaves and the prediction is generated immediately.  
- **Heuristics**: Traditional mildew detection relies on visual inspection, which require a lot resources in terms of labour and time. The ML model provides a consistent, efficient assessment and supports the client in making timely decisions.  
- **Training data:** curated dataset of plant leaf images, including healthy and mildew-infected leaves.  
  - **Target:** infected or not; **Features:** all images.  

## Dashboard Design

The Streamlit dashboard is organized into the following pages:

| Page | Description  |
|------|------------- |
| **Project Summary** | Introduces the problem and dataset characteristics. |
| **Leaf Visualiser** | Allows users to explore examples and visual comparisons between healthy and infected leaves. |
| **Powdery Mildew Detector** | Upload and classify new leaf images, with an optional downloadable prediction report. |
| **Project Hypothesis** | Outlines assumptions and reasoning related to visual and model-based diagnosis. |
| **Model Performance Evaluation** | Displays metrics, confusion matrix, ROC curve, and interpretation of model behavior. |

### Page 1: Project Summary

<details>
<summary>Project Summary</summary>

![Project Summary](./docs/readme_images/screenshots/screenshot-project-summary.png)
</details>

- General Information
  - Mildew is a fungal infection affecting plant leaves, reducing crop yield and plant health.
  - Early detection allows timely intervention, such as targeted treatment or pruning, preventing spread to other plants.
  - Accurate diagnosis of mildew is challenging with visual inspection alone and can be affected by human error or inexperience.
- Project Dataset
  - The dataset contains labeled images of healthy and mildew-infected leaves, curated from various plant species to train the ML model.
- Link to additional information
- Business requirements
  - The client is interested in visually differentiating between healthy and mildew-infected leaves.
  - The client is interested in receiving an automated assessment of whether a leaf is infected.

### Page 2: Leaf Visualizer

<details>
<summary>Leaf Visualizer</summary>

![Leaf Visualizer](./docs/readme_images/screenshots/screenshot-leaf-visualizer.png)
</details>

- Answers Business Requirement 1: Primarily images
  - Checkbox 1 – Difference between average and variability images
  - Checkbox 2 – Differences between average infected and average healthy leaves
  - Checkbox 3 – Generate random image montage (select label: healthy or infected and layout type)

### Page 3: Mildew Detector

<details>
<summary>Mildew Detector</summary>

![Mildew Detector](./docs/readme_images/screenshots/screenshot-mildew-detector.png)
</details>

- Answers Business Requirement 2: Presents an interative tool to predict if a given leaf image is healthy or infected with powdery mildew.
- User Interface
  - File uploader widget for multiple leaf images
  - Display each image with prediction statement: infected or healthy, with associated probability
- Table showing image names and prediction results
- Download button to export table as CSV

### Page 4: Project Hypotheses and Validation

<details>
<summary>Project Hypotheses and Validation</summary>

![Project Hypotheses](./docs/readme_images/screenshots/screenshot-project-hypothesis.png)
</details>

- Hypothesis 1: There are clear visual markers or characteristics that distinguish healthy cherry leaves from those infected with powdery mildew.
- Hypothesis 2: A Convolutional Neural Network (CNN) can learn to recognize the visual differences between healthy and infected leaves accurately.

### Page 5: ML Performance Metrics

<details>
<summary>ML Performance Metrics</summary>

![ML Performance](./docs/readme_images/screenshots/screenshot-ml-performance.png)
</details>

- Label Distribution Overview
- Model Training History - Accuracy and losses
- Model Evaluation Results
- ROC Curve and AUC Score

## User stories and Testing

- **Intuitive Navigation**
  - As a client, I want a user-friendly dashboard with a clear and intuitive navigation so that I can find specific information about the application

  - **Feature Test**

  | Feature | Action | Expected Result | Actual Result |
  | ------- |------- | --------------- | --------------- |
  | Expand/collapse side navigation | click on the navigation arrow | side navigation expands (collapses) | results as expected |
  | Navigation items | click on any page heading in the navigation menu | Selected page is displayed with the relevant content | results as expected |

- **Leaf Visualizer - Business Requirement 1**
  - As a client, I can view average, variability and difference images so that I can better understand how infected and healthy leaves differ visually.

  - **Feature Test**

  | Feature | Action | Expected Result | Actual Result |
  | ------- |------- | --------------- | --------------- |
  | Average and variability images checkbox | check the checkbox | Average and variability images are rendered below the checkbox | results as expected |
  | Average difference image checkbox | check the checkbox | Average and difference images are rendered below the checkbox | results as expected |

  - As a client, I can generate a random image montage so that I can view multiple leaf images for infected and healthy leaves.

  - **Feature Test**

  | Feature | Action | Expected Result | Actual Result |
  | ------- |------- | --------------- | --------------- |
  | Image montage  checkbox| check the 'Image Montage'checkbox | Two dropdown select menus are rendered. One for label (health  or infected) and the other for layout. 'Create Montage' button is displayed below the checkboxes | results as expected |
  | Create image montage button | Click the 'Create Montage' button | Image montage for the specified label and layout is rendered | results as expected |

- **Powdery Mildew Detector- Business Requirement 2**
  - As a client, I can upload image(s) of cherry leaves and get a live prediction on each of the predicted images.

  - **Feature Test**

  | Feature | Action | Expected Result | Actual Result |
  | ------- |------- | --------------- | --------------- |
  | Image file uploader | upload one or more leaf images | immediate feedback with results for each image and associated probability for the outcome label | results as expected |
  | Upload '.png', 'jpg', 'jpeg' image formats | upload images of different formats | predictions are given for each image in a table | results as expected |

  - As a client, I can download the table predictions as a csv so that I can use the results later.

  - **Feature Test**

  | Feature | Action | Expected Result | Actual Result |
  | ------- |------- | --------------- | --------------- |
  | Download Report Link | Click 'Download Report' link | A csv file containing current prediction results is downloaded automatically | results as expected |  

## Code validation

| Script Tested | Screenshot of Errors | Solution Applied   | Screenshot of Clear Validator Output |  
|------------  |------------ |------------ |------------ |
| multipage.py | <img src="docs/readme_images/validation/multipage-pep8-initial-validator-results.png" width="500px"> | **error:** Missing spaces and lines that were too long were all fixed. | <img src="docs/readme_images/validation/multipage-pep8-final-validator-results.png" width="500px"> |
| page_leaf_visualiser.py  | <img src="docs/readme_images/validation/page-leaf-visualiser-pep8-initial-validator-results.png" width="500px"> | **error:** Missing spaces and lines that were too long were all fixed. | <img src="docs/readme_images/validation/page-leaf-visualiser-pep8-final-validator-results.png" width="500px"> |
| page_ml_performance.py  | <img src="docs/readme_images/validation/page-ml-performance-pep8-initial-validator-results.png" width="500px"> | **error:** Missing spaces and lines that were too long were all fixed. | <img src="docs/readme_images/validation/page-ml-performance-pep8-final-validator-results.png" width="500px"> |
| page_powdery_mildew_detector.py  | <img src="docs/readme_images/validation/page-mildew-detector-pep8-initial-validator-results.png" width="500px"> | **error:** Missing spaces and lines that were too long were all fixed. | <img src="docs/readme_images/validation/page-mildew-detector-pep8-final-validator-results.png" width="500px"> |
| page_project_hypothesis.py  | <img src="docs/readme_images/validation/page-project-hypotheses-pep8-initial-validator-results.png" width="500px"> | **error:** Missing spaces and lines that were too long were all fixed. | <img src="docs/readme_images/validation/page-project-hypotheses-pep8-final-validator-results.png" width="500px"> |
| page_summary.py  | <img src="docs/readme_images/validation/page-summary-pep8-initial-validator-results.png" width="500px"> | **error:** Missing spaces and lines that were too long were all fixed. | <img src="docs/readme_images/validation/page-summary-pep8-final-validator-results.png" width="500px"> |
| evaluate_clf.py  | <img src="docs/readme_images/validation/evaluate-pep8-initial-validator-results.png" width="500px"> | **error:** Missing spaces and lines that were too long were all fixed. | <img src="docs/readme_images/validation/evaluate-pep8-final-validator-results.png" width="500px"> |
| predictive_analysis.py  | <img src="docs/readme_images/validation/predictive-analysis-pep8-initial-validator-results.png" width="500px"> | **error:** Missing spaces and lines that were too long were all fixed. | <img src="docs/readme_images/validation/predictive-analysis-pep8-final-validator-results.png" width="500px"> |
| data_management.py  | <img src="docs/readme_images/validation/data-management-pep8-initial-validator-results.png" width="500px"> | **error:** Missing spaces and lines that were too long were all fixed. | <img src="docs/readme_images/validation/data-management-pep8-final-validator-results.png" width="500px"> |
| app.py  | <img src="docs/readme_images/validation/app-pep8-initial-validator-results.png" width="500px"> | **error:** Missing spaces and lines that were too long were all fixed. | <img src="docs/readme_images/validation/app-pep8-final-validator-results.png" width="500px"> |
| style.css  | <img src="docs/readme_images/validation/style-css-initial-validator-results.png" width="500px"> | No errors or warnings | No further changes |

## Bugs

- **Incorrect class label mapping (RESOLVED):** The class labels were being read from directory names in an inconsistent order, which led to reversed label assignments during training and prediction. This was resolved by applying `.sort()` to the label list.
- **Complied slug size error (UNRESOLVED):** When deploying to Heroku, an error occurred due to the compiled slug size exceeding the 500 MB limit. Tried resolving this issue by adding unnecessary files and folders to the .slugignore file and keeping only the required libraries in the requirements.txt file. There was no resoltuion to the Heroku limit error. In the end, the final dashboard was deployed on streamlit platform - [Powdery Mildew Detector - Streamlit](https://detect-mildew-in-cherry-leaves-2zq3hwsa6w44mqxdq9d9vd.streamlit.app/)

## Deployment

### Heroku - NOT USED

The project was initially planned for deployment on Heroku, but the app could not be compiled successfully because the final slug size exceeded Heroku's maximum allowed limit. Even after removing non-essential files and using a .slugignore file, the build remained too large for Heroku.

Deployment was abandoned due to these platform limitations. Streamlit.io was used as the hosting option for the live dashboard.

1. Log in to Heroku and create an App
2. At the Deploy tab, select GitHub as the deployment method.
3. Select your repository name and click Search. Once it is found, click Connect.
4. Select the branch you want to deploy, then click Deploy Branch.
5. The deployment process should happen smoothly if all deployment files are fully functional. Click the button Open App on the top of the page to access your App.
6. If the slug size is too large, then add large files not required for the app to the .slugignore file.

### Streamlit

1. Log in to [streamlit.io](https://streamlit.io/) and click 'Create App'
2. Under 'Deploy a public app from GitHub' click 'Deploy now'
3. Connect your GitHub account if it is not connected already.
4. Select the repository that contains your Streamlit project or paste the GitHub URL to your repository.
5. Choose the branch and the main script file (e.g., app.py).
6. Review the deployment settings. Streamlit Cloud automatically detects required packages from requirements.txt.
7. Click on 'Advanced settings' and specify the python version for running the application
8. Click Deploy to launch the app.
9. Once the build finishes, the app will launch in a new window. Any future commits to the repository will trigger an automatic redeployment.

## Main Data Analysis and Machine Learning Libraries

- **[NumPy](https://numpy.org/)** – Used to handle numerical data and image arrays. E.g. images were converted to NumPy arrays for preprocessing before training the model.
- **[Pandas](https://pandas.pydata.org/)** – Helpful for organizing and analyzing data. E.g. pandas `DataFrames` were used to store image metadata and model evaluation results.
- **[Matplotlib](https://matplotlib.org/)** – Used to plot images and visualize performance metrics. E.g. used to create plots.
- **[Seaborn](https://seaborn.pydata.org/)** – Extends Matplotlib library for styled plots. E.g. used to create plots.
- **[Plotly](https://plotly.com/python/)** – Added interactivity to visualizations in the dashboard. E.g. used to create interactive charts for exploring dataset characteristics.
- **[TensorFlow](https://www.tensorflow.org/)** – The main deep learning library used to build and train the CNN model. E.g. the CNN was trained with TensorFlow to detect powdery mildew on cherry leaves.
- **[Keras Tuner](https://keras.io/keras_tuner/)** – Used to fine-tune hyperparameters for improved model performance. E.g. Helped find the best combination of dropout rate, and number of filters.
- **[Scikit-learn](https://scikit-learn.org/)** – Provided tools for evaluation and performance reporting. E.g. generated classification reports, confusion matrices, and key metrics for model evaluation.
- **[Pillow (PIL)](https://pillow.readthedocs.io/)** – Used for image manipulation tasks. E.g. used to load and resize images before converting them into NumPy arrays.

## Other Technologies Used

- **[Streamlit](https://streamlit.io/)** – Framework for creating the interactive dashboard.
- **[Git & GitHub](https://github.com/)** – Version control and repository hosting.  
- **[Codespaces](https://github.com/features/codespaces/)** – the github cloud-based IDE used throughout the project.
- **[Am I Responsive](https://ui.dev/amiresponsive)** – Used to create the application mock view.

## Limitations and Considerations

- The training images were taken in controlled conditions with a clean, uniform background. When the model is given images with shadows, other leaves, or different objects in the frame, predictions may be less accurate - see table below.
- Real-world photos often vary in lighting, angles, and background, which can make classification more challenging.
- Early signs of infection can be very faint, and the model performance might not always be reliable in such instances.
- Expanding the dataset or using more diverse training images could help improve the model's reliability.

| Image Content | Image | Expected Result | Actual Result |
| ------------- | ------| --------------- | ------------- |
| Multiple leaves (infected) | <img src="docs/readme_images/test/mildew-true-predict.png" width="500px">  | Infected | Infected |
| Multiple leaves (Healthy) | <img src="docs/readme_images/test/healthy-false-predict.png" width="500px"> | Healthy  | Infected |

## Credits

- The project was primarily adapted from the [Code Institute "Malaria Detector" walkthrough](https://github.com/tumelo-maja/malaria-image-detection), which guided the structure of the notebooks, the Streamlit dashboard layout, the model workflow, and the reporting functionality.
- The [Brain Tumor Detector](https://github.com/tomdu3/brain-tumor-detector) repository helped with organising the project directory and understanding how to build a clean, modular prediction pipeline for image classification.
- A [Streamlit CSS-customisation youtube tutorial](`https://www.youtube.com/watch?v=jbJpAdGlKVY`) was used as a guide for styling dashboard pages using custom CSS.

## Acknowledgements

- Thanks to my mentor, Mo Shami, for his guidance and steady support throughout the project.
- Tutors at Code Institute for their help and support when troubleshooting code errors.
- Great thanks you to my friends and family for their patience and support while I completed this project.
