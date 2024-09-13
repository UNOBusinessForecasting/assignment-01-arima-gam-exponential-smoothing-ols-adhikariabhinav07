#Import statements
import pandas as pd
import numpy as np
import statsmodels.formula.api as smf
import statsmodels.tsa.stattools as st
import plotly.express as px
import patsy as pt

train_data = pd.read_csv(
    "https://github.com/dustywhite7/econ8310-assignment1/raw/main/assignment_data_train.csv")
eqn = 'trips ~ month+day+hour'
y, x = pt.dmatrices(eqn, train_data)
model = LinearGAM(s(0) + s(1) + s(2) + s(3) )
modelFit = model.gridsearch(np.asarray(x), y)
modelFit.summary()

pred = modelFit.predict(np.asarray(x) )
pred
