#Import statements
import pandas as pd
import numpy as np
import statsmodels.formula.api as smf
import statsmodels.tsa.stattools as st
import plotly.express as px

train_data = pd.read_csv(
    "https://github.com/dustywhite7/econ8310-assignment1/raw/main/assignment_data_train.csv")
eqn = 'trips ~ month+day+hour'
y, x = pt.dmatrices(eqn, train_data)
gam = LinearGAM(s(0) + s(1) + s(2) + s(3) )
gam = gam.gridsearch(np.asarray(x), y)
gam.summary()

pred = gam.predict(744)
pred
