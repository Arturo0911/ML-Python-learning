import math
from pprint import pprint
import random
from concurrent.futures import ThreadPoolExecutor
from types import new_class 
import pandas as pd
import numpy as np
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
import matplotlib.pyplot as plt
from sklearn.metrics import classification_report
from sklearn import preprocessing
from sklearn import utils

dataframe = pd.read_csv('.csv/.clouds_parameters/.Overcast_clouds/.2017/.2017.csv')


dataframe_test = pd.read_csv('.csv/.clouds_parameters/.Overcast_clouds/.2018/.2018.csv')
# dataframe.drop(['time_start', 'time_end','cloud_description','precip', 'icon', 'code'], axis=1, inplace=True)
# dataframe.drop(['time_start', 'time_end','cloud_description','clouds','precip', 'icon', 'code'], axis=1, inplace=True)


df = dataframe[dataframe['temperature'] > 0]

X = df.drop(['time_start', 'time_end','cloud_description','relative_humidity','precip', 'icon', 'code'], axis=1)
print(X)
#X = dataframe.drop('relative_humidity', axis=1).dropna(axis=0, how ='any')
y = df['relative_humidity']
print(y)
X_train,X_test, y_train, y_test= train_test_split(X, y, test_size= 0.3)
log_model = LogisticRegression()
log_model.fit(X_train, y_train.astype('long'))
# print(type(X))
# print(type(y))

'''X_train,X_test, y_train, y_test= train_test_split(X, y, test_size= 0.3, random_state= 101)


log_model = LogisticRegression()
log_model.fit(X_train, y_train.astype('long'))
predictions = log_model.predict(X_test)
print(classification_report(y_test.astype('long'), predictions))
# y = dataframe['temperature'].dropna(axis= 1, how ='any')'''

'''
X_train,X_test, y_train, y_test= train_test_split(X, y, test_size= 0.4, random_state= 101)
log_model = LogisticRegression()
log_model.fit(X_train, y_train)
predictions = log_model.predict(X_test)

lab_enc = preprocessing.LabelEncoder()
training_scores_encoded = lab_enc.fit_transform(y_train)
print(training_scores_encoded)
print(utils.multiclass.type_of_target(y_train))
print(utils.multiclass.type_of_target(y_train.astype('int')))
print(utils.multiclass.type_of_target(training_scores_encoded))
'''



'''
try:
    log_model = LogisticRegression(max_iter = 1000)
    log_model.fit(X_train, training_scores_encoded)
    predictions = log_model.predict(X_test)
    print("here")
    print(predictions)
    print(classification_report(y_test, predictions))

except Exception as e:
    print("The exceptins is by: ",str(e))

log_model = LogisticRegression()

log_model.fit(X_train, y_train)

predictions = log_model.predict(X_test)

print(predictions)
'''