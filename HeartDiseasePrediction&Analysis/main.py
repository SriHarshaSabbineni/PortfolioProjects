# import numpy as np
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
import pickle
import seaborn as sns

heart_data = pd.read_csv('C:/Users/navee/PycharmProjects/mlpython/heart.csv')
print(heart_data.head())
print(heart_data.tail())
print(heart_data.shape)
print(heart_data.info())
print(heart_data.isnull().sum())
print(heart_data['target'].value_counts())
# sns.heatmap(heart_data.corr())

#splitting the features and target
X = heart_data.drop(columns='target', axis=1)
print(X)
Y = heart_data['target']
print(Y)

#splitting data into training data and testing data
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, stratify=Y, random_state=1)
print(X.shape, X_train.shape, X_test.shape)
print(Y.shape, Y_train.shape, Y_test.shape)

#training the model
model = LogisticRegression()

model.fit(X_train, Y_train)

#model evaluation

X_train_prediction = model.predict(X_train)
training_data_accuracy = accuracy_score(X_train_prediction, Y_train)
print('training_data_accuracy:', training_data_accuracy)

X_test_prediction = model.predict(X_test)
testing_data_accuracy = accuracy_score(X_test_prediction, Y_test)
print('testing_data_accuracy:', testing_data_accuracy)

# input_data=(62,0,0,138,294,1,1,106,0,1.9,1,3,2)
# input_data_as_np_array=np.asarray(input_data)
# print(input_data_as_np_array.shape)
# reshaped_data=input_data_as_np_array.reshape(1,-1)
# print(reshaped_data.shape)
# prediction = model.predict(reshaped_data)
# print(prediction)
#
# filename = 'trained_model.sav'
# pickle.dump(model, open(filename,'wb'))

