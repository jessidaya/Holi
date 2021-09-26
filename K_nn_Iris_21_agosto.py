#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug 21 11:45:24 2021

@author: miguelabecerrab
"""
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import classification_report, confusion_matrix

url="https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data"

encabezado=['sepal-length', 'sepal-width', 'petal-length', 'petal-width','Class']
dataset=pd.read_csv(url, names=encabezado)

dataset.head()

X=dataset.iloc[:,0:4]
Y=dataset.iloc[:,4]


X_train, X_test, y_train, ytest= train_test_split(X,Y, test_size=0.2)

scaler=StandardScaler()
scaler.fit(X_train)

X_train=scaler.transform(X_train)
X_test=scaler.transform(X_test)

classifier=KNeighborsClassifier(n_neighbors=5)
classifier.fit(X_train,  y_train)


y_pred=classifier.predict(X_test)



desempeno=confusion_matrix(ytest, y_pred)

resumen=classification_report(ytest, y_pred)












