import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
import pickle

loaded_model = pickle.load(open('trained_model.sav','rb'))
input_data=(62,0,0,138,294,1,1,106,0,1.9,1,3,2)
input_data_as_np_array=np.asarray(input_data)
reshaped_data=input_data_as_np_array.reshape(1,-1)
prediction = loaded_model.predict(reshaped_data)
print(prediction)