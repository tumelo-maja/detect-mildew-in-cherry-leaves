import streamlit as st
import os
import random
import itertools
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib.image import imread

import itertools
import random

def page_leaf_visualiser_body():
    st.write("## Leaf Visualiser")
    st.info(
       "The main goal is to visually differentiate leaves affected by powdery mildew from healthy ones.\n\n"
        " Healthy cherry leaves usually have a smooth and even green surface. "
        "Infected leaves may show pale spots or a thin, powdery white coating. "
        "These are the visual differences the model is trained to identify.\n\n"
        )
    
    version = "v2"

    if st.checkbox("Show average and variability images"):
        avg_infected = plt.imread(f"outputs/{version}/average_variability_powdery_mildew.png")
        avg_healthy = plt.imread(f"outputs/{version}/average_variability_healthy.png")

        st.image(avg_infected, caption="Infected Leaves - Average and Variability")
        st.image(avg_healthy, caption="Healthy Leaves - Average and Variability")
        st.write("---")

    if st.checkbox("Show difference between average infected and healthy leaves"):
        diff = plt.imread(f"outputs/{version}/average_difference.png")
        st.image(diff, caption="Difference Between Average Images")
        st.write("---")

    if st.checkbox("Create Image Montage"):
        data_dir = "inputs/mildew_dataset/cherry-leaves/validation"
        labels = os.listdir(data_dir)
        label = st.selectbox("Select label:", labels)
        title_str = "Powder Mildew: Infected Leaves" if 'mildew' in label else "Healthy Leaves"

        selected_size = st.selectbox( "Choose montage layout",
            ["2 x 2", "2 x 3", "3 x 3"],
            index=1)
        size_options = {"2 x 2": (2, 2),"2 x 3": (2, 3),"3 x 3": (3, 3)}
        nrows, ncols = size_options[selected_size]

        if st.button("Create Montage"):
            image_montage(dir_path=data_dir, label_to_display=label, nrows=nrows, ncols=ncols, fig_width=10, title_str=title_str)
        st.write("---")


def image_montage(dir_path, label_to_display, nrows, ncols, fig_width=10, title_str=''):
  sns.set_style("white")
  labels = os.listdir(dir_path)

  # subset the class you are interested to display
  if label_to_display in labels:

    # checks if your montage space is greater than subset size
    # how many images in that folder
    images_list = os.listdir(dir_path+'/'+ label_to_display)
    if nrows * ncols < len(images_list):
      img_idx = random.sample(images_list, nrows * ncols)
    else:
      print(
          f"Decrease nrows or ncols to create your montage. \n"
          f"There are {len(images_list)} in your subset. "
          f"You requested a montage with {nrows * ncols} spaces")
      return
    

    # create list of axes indices based on nrows and ncols
    list_rows= range(0,nrows)
    list_cols= range(0,ncols)
    plot_idx = list(itertools.product(list_rows,list_cols))


    # create a Figure and display images
    img = imread(dir_path + '/' + label_to_display + '/' + img_idx[0])
    img_height, img_width = img.shape[:2]
    fig_height = fig_width * (img_height / img_width) * nrows / ncols   

    fig, axes = plt.subplots(nrows=nrows,ncols=ncols, figsize=(fig_width, fig_height))
    for x in range(0,nrows*ncols):
      img = imread(dir_path + '/' + label_to_display + '/' + img_idx[x])
      axes[plot_idx[x][0], plot_idx[x][1]].imshow(img)
      axes[plot_idx[x][0], plot_idx[x][1]].set_xticks([])
      axes[plot_idx[x][0], plot_idx[x][1]].set_yticks([])
    plt.tight_layout() 
    fig.suptitle(title_str, fontsize=20, y=1.05)
    st.pyplot(fig=fig)

  else:
    print("The label you selected doesn't exist.")
    print(f"The existing options are: {labels}")