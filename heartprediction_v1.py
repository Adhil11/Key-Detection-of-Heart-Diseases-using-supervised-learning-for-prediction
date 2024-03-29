# -*- coding: utf-8 -*-
"""Copy_of_HeartPrediction_V1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1KK71vVTvNR9OrFzKvKlOW9RxGID3_SsQ
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix
from sklearn.metrics import f1_score
from sklearn.model_selection import train_test_split
import warnings
warnings.filterwarnings('ignore')
import sklearn.neighbors
from sklearn.neighbors import KNeighborsClassifier
import statsmodels.api as sm
from sklearn.datasets import load_iris
from sklearn.naive_bayes import GaussianNB
classifier = GaussianNB()
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.model_selection import GridSearchCV
from matplotlib.pylab import rcParams
rcParams['figure.figsize'] = 12, 4
from sklearn.model_selection import KFold
from sklearn.metrics import classification_report
from sklearn import svm
from sklearn.svm import LinearSVC
import cvxopt
from sklearn.tree import DecisionTreeClassifier
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.tree import export_graphviz
from IPython.display import Image
import pydotplus
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Conv2D, Dropout, Flatten, MaxPooling2D
import os
import itertools
import random
from sklearn.ensemble import AdaBoostClassifier
from sklearn import metrics

import io

from google.colab import files
uploaded = files.upload()

data = pd.read_csv(io.BytesIO(uploaded['Heart_Disease_Prediction.csv (1).xls']))

abc = AdaBoostClassifier(n_estimators=50,
                         learning_rate=1)
# Train Adaboost Classifer

data

x = data.iloc[:, :-2]
y = data.iloc[:, -1]
x_train, x_test, y_train, y_test = train_test_split(x, y, random_state = 0, test_size = 0.35)

sc_x = StandardScaler()
x_train = sc_x.fit_transform(x_train)
x_test = sc_x.transform(x_test)

import math
math.sqrt(len(y_test))

classifier = KNeighborsClassifier(n_neighbors = 9, p = 2, metric = 'euclidean')
classifier.fit(x_train,y_train)
y_pred = classifier.predict(x_test)
y_pred
cm = confusion_matrix(y_test,y_pred)
print(accuracy_score(y_test,y_pred))

clf = svm.SVC(kernel='rbf')
clf.fit(x_train,y_train)
y_pred = clf.predict(x_test)
y_pred = clf.predict(x_test)
y_pred
cm = confusion_matrix(y_test,y_pred)
print(accuracy_score(y_test,y_pred))

classifier.fit(x_test, y_test)
y_pred  =  classifier.predict(x_test)
y_pred
ac = accuracy_score(y_test,y_pred)
print(ac)

kf = KFold(n_splits=5,random_state=42,shuffle=True)
gradient_booster = GradientBoostingClassifier(learning_rate=0.1)
gradient_booster.get_params()
gradient_booster.fit(x_train,y_train)
print(classification_report(y_train,gradient_booster.predict(x_train)))

svc = LinearSVC()
svc.fit(x_train, y_train)
y_pred = svc.predict(x_test)
y_pred
ac = accuracy_score(y_test,y_pred)
print(ac)

clf = DecisionTreeClassifier()
clf = clf.fit(x_train,y_train)
y_pred = clf.predict(x_test)
print("Accuracy:",accuracy_score(y_test, y_pred))

input_shape = (28, 28, 1)
model = Sequential()
model.add(Conv2D(28, kernel_size=(3,3), input_shape=input_shape))
model.add(MaxPooling2D(pool_size=(2, 2)))
model.add(Flatten()) # Flattening the 2D arrays for fully connected layers
model.add(Dense(128, activation=tf.nn.relu))
model.add(Dropout(0.2))
model.add(Dense(10,activation=tf.nn.softmax))

model = abc.fit(x_train, y_train)

#Predict the response for test dataset
y_pred = model.predict(x_test)
print("Accuracy:",metrics.accuracy_score(y_test, y_pred))