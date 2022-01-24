#!/usr/bin/env python
# coding: utf-8

# In[1]:


import streamlit as st
import pandas as pd
import numpy as np

from pywaffle import Waffle
import matplotlib.pyplot as plt

# Add a selectbox to the sidebar:
TP = st.sidebar.number_input('True positive', value = 306)
FN = st.sidebar.number_input('False negative', value = 23)
TN = st.sidebar.number_input('True negative', value = 2909)
FP = st.sidebar.number_input('False positive', value = 197)

# viz_selectbox = st.sidebar.selectbox(
#     'Type of Visualization',
#     ('Email', 'Home phone', 'Mobile phone')
# )

# Add a slider to the sidebar:
vsize_slider = st.sidebar.slider(
    'Vertical figure size',
    0, 50, value = 20,
)

hsize_slider = st.sidebar.slider(
    'Horizontal figure size',
    0, 50, value = 20,
)

rows_slider = st.sidebar.slider(
    'Number of rows in figure',
    0, 100, value = 50,
)

title_fontsize_slider = st.sidebar.slider(
    'Title font size',
    0, 50, value = 25,
)

legend_fontsize_slider = st.sidebar.slider(
    'Legend font size',
    0, 50, value = 25,
)

# 'TP: ', TP
# 'FN: ', FN
# 'TN: ', TN
# 'FP: ', FP

#test = {'True positive' :306, 'False negative': 23, 'True negative': 2909, 'False positive': 197, }

test = {'False negative': FN, 'True positive' :TP, 'False positive': FP, 'True negative': TN, }

# plotting of confusion matrix
fig = plt.figure(
    FigureClass=Waffle,
    figsize = (vsize_slider,hsize_slider),
    values=test,
    title={
        'label': 'Confusion Matrix Icon Array',
        'loc': 'center',
        'fontdict': {
            'fontsize': title_fontsize_slider
        }
    },
    rows=rows_slider,
    icons=['circle','bullseye','bullseye','circle'],
    icon_style=['regular','solid', 'solid','regular'],
    colors=('lightcoral','lightcoral','cornflowerblue','cornflowerblue'),
    starting_location='NW',
    labels=[f"{k} ({v})" for k, v in test.items()],
    legend={'bbox_to_anchor':(1,1), 'loc':'upper left', 'fontsize': legend_fontsize_slider},
    icon_legend = True,
)

st.header('Create Icon Array from Confusion Matrix')

st.pyplot(fig)

accuracy = (TP+TN)/(TP+TN+FP+FN)
precision = TP/(TP+FP)
recall = TP/(TP+FN) #True positive rate
specificity = TN/(TN+FP) #True negative rate
F1_score = 2*(precision*recall)/(precision+recall)

st.write('Accuracy:', accuracy)
st.write('Precision:', precision)
st.write('Recall:', recall)
st.write('Specificity:', specificity)
st.write('F1-score:', F1_score)

# st.plotly_chart(fig)
