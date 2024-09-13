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
model = sm.tsa.arima.ARIMA(y, seasonal_order=(1,1,0,24), exog=x)
reg = model.fit()
pred = reg.forecast(steps=744, exog=x[-744:]) 
