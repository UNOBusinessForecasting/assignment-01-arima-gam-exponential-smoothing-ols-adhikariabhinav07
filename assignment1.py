#Import statements
import pandas as pd
import numpy as np
from pygam import LinearGAM, s

train_data = pd.read_csv("https://github.com/dustywhite7/econ8310-assignment1/raw/main/assignment_data_train.csv")
x = train_data[['hour', 'day', 'month']]
y = train_data['trips']
model = LinearGAM(s(0) + s(1) + s(2) + s(3) )
modelFit = model.gridsearch(np.asarray(x), y)


pred = modelFit.predict(np.asarray(x) )

print(modelFit.summary())
pred
