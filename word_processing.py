# Import Library of Gaussian Naive Bayes model
from sklearn.naive_bayes import GaussianNB
import numpy as np


x = np.array()
Y = np.array()
model = GaussianNB()

# Тренировка модели
model.fit(x, y)

# Predict Output
predicted = model.predict()
print(predicted)
