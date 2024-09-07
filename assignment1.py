import pandas as pd
import numpy as np
import statsmodels.formula.api as smf
import statsmodels.tsa.stattools as st
import plotly.express as px

# Prep the dataset
data = pd.read_csv("https://github.com/dustywhite7/econ8310-assignment1/raw/main/assignment_data_train.csv")

reg = smf.ols("trips ~ Timestamp", data=data)
reg = reg.fit()
print(reg.summary())
