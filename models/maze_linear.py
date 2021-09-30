import pandas as pd
import numpy as np

import matplotlib.pyplot as plt

import seaborn as sns

from sklearn.svm import LinearSVC
from sklearn.model_selection import train_test_split
from sklearn.model_selection import cross_val_score
from sklearn.metrics import confusion_matrix
from sklearn.metrics import classification_report

import joblib

dfs = []
for j in ['maze.json']:
    data = pd.read_json(j)
    dfs.append(data)

dataset = pd.concat(dfs, ignore_index=True)
print(dataset.shape)
print(dataset.head())
print(dataset.describe())

print(dataset.columns)

x = dataset[['R_sensor', 'L_sensor', 'F_sensor']]
y = dataset['direction']
#y = dataset[['left_PWM', 'right_PWM']]

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2)

model = LinearSVC(verbose=0, max_iter=100000)
#model = LinearSVC(verbose=0)
print(model)

model.fit(x_train, y_train)
score = model.score(x_train, y_train)
print("Score: ", score)

cv_scores = cross_val_score(model, x_train, y_train, cv=10)
print("CV average score: %.2f" % cv_scores.mean())

ypred = model.predict(x_test)

#cm = confusion_matrix(y_test, ypred)
#print(cm)

#cr = classification_report(y_test, ypred)
#print(cr)

joblib.dump(model, 'LSVC_model')
