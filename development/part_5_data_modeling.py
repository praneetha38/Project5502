# -*- coding: utf-8 -*-
"""Part 5 - Data Modeling.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1J76p_sLz16jwYsOklQ7ETQD5IaaSx2O_

# Part 5 - Data Modeling

## Get Data
"""

# seed
import random

seed_id = 123456789
random_state = random.seed(seed_id)
random_state

import shutil

# Source file path (within your Drive)
source_file = '/content/drive/MyDrive/Colab Notebooks/train_test_split.pkl'

# Destination path (root of your Drive)
destination_path = 'train_test_split.pkl'

# Copy the file
shutil.copy(source_file, destination_path)

import pickle

# Load the data
with open('.../train_test_split.pkl', 'rb') as f:
    X_train, X_test, y_train, y_test = pickle.load(f)

"""## Logistic Regression"""

# model, predict, evaluate, and plot
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix, accuracy_score

model = LogisticRegression(solver='liblinear', random_state=random_state)
model.fit(X_train, y_train)
predictions = model.predict(X_test)

print(confusion_matrix(y_test, predictions))
print(accuracy_score(y_test, predictions))

"""## Random Forest"""

from sklearn.ensemble import RandomForestClassifier

model = RandomForestClassifier(n_estimators=100, criterion='entropy', random_state=random_state)
model.fit(X_train, y_train)
predictions = model.predict(X_test)

print(confusion_matrix(y_test, predictions))
print(accuracy_score(y_test, predictions))

"""## Model Evaluation"""

from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

tn, fp, fn, tp = confusion_matrix(y_test, predictions).ravel()
print('accuracy:', accuracy_score(predictions, y_test))
print(confusion_matrix(y_test, predictions))
print(classification_report(y_test, predictions))

"""## Model Fine-Tuning"""

from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import GridSearchCV

hyperparameters = {'max_depth': [2, 3],
              'min_samples_split': [4, 5],
              'min_samples_leaf': [4, 5],
              'bootstrap': [True, False],
              'criterion': ['entropy', 'gini']}

grid_search = GridSearchCV(estimator = RandomForestClassifier(),
                           param_grid = hyperparameters,
                           scoring = 'accuracy',
                           cv = 10)

grid_search = grid_search.fit(X_train, y_train)

best_accuracy = grid_search.best_score_
best_parameters = grid_search.best_params_

print('best accuracy', best_accuracy)
print('best parameters', best_parameters)

"""## Final Model"""

from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

model = RandomForestClassifier(random_state=random_state).set_params(**best_parameters) # * args, ** kwargs
model.fit(X_train.values, y_train)
predictions = model.predict(X_test.values)
print('accuracy:', accuracy_score(predictions, y_test))

"""## Confusion Matrix"""

print(confusion_matrix(y_test, predictions))

"""## Precision Recall"""

print(classification_report(y_test, predictions))

"""## Bias Variance"""

from mlxtend.evaluate import bias_variance_decomp

avg_expected_loss, avg_bias, avg_var = bias_variance_decomp(
    model,
    X_train.values, # Convert X_train to NumPy array
    y_train.values, # Convert y_train to NumPy array
    X_test.values, # Convert X_test to NumPy array
    y_test.values, # Convert y_test to NumPy array
    loss='0-1_loss',
    random_seed=random_state)

print('Average expected loss: %.3f' % avg_expected_loss)
print('Average bias: %.3f' % avg_bias)
print('Average variance: %.3f' % avg_var)

# Average expected loss: 0.087
# Average bias: 0.080
# Average variance: 0.034

X_test.head()

import pandas as pd

sample_to_predict = pd.Series({"watch_time": -8.1, "avg_view_duration": 1.4, "click_through_rate": -0.7, "interest": 0})
sample_to_predict = pd.DataFrame([sample_to_predict])
model.predict_proba(sample_to_predict.values)

import pickle

with open('.../model.pkl', 'wb') as file:
    pickle.dump(model, file)

import shutil

# Source file path (within your Drive)
source_file = 'model.pkl'

# Destination path (root of your Drive)
destination_path = '/content/drive/MyDrive/Colab Notebooks/model.pkl'

# Copy the file
shutil.copy(source_file, destination_path)