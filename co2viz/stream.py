import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = pd.read_csv('mars-2014-complete-cleaned.csv')


quantitative_columns = data.select_dtypes(include=[np.number]).columns
x = st.selectbox('Select x-axis', quantitative_columns)
y = st.selectbox('Select y-axis', quantitative_columns)

qualitative_columns = data.select_dtypes(include=['object']).columns
split_by = st.selectbox('Split by', qualitative_columns)

if st.button('Plot'):

    fig, ax = plt.subplots()


    values = data[split_by].unique()
    n = len(values)
    colors = plt.cm.viridis(np.linspace(0, 1, n))
    st.write(colors)

    fig, ax = plt.subplots(1, 1, figsize=(14, 8))
    for color, value in zip(colors, values):
        subset = data[data[split_by] == value]
        ax.scatter(
            subset[x],
            subset[y],
            color=color,
            label=value,
            alpha=0.4,
            s=10
        )

    ax.legend()
    ax.set_xlabel(x)
    ax.set_ylabel(y)

    st.pyplot(fig)