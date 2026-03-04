from sklearn.ensemble import IsolationForest
import numpy as np

model = IsolationForest(contamination=0.1)

training_data = np.array([
    [10],
    [12],
    [15],
    [8],
    [11],
    [9],
    [300]
])

model.fit(training_data)

def detect_anomaly(requests_per_minute):

    prediction = model.predict([[requests_per_minute]])

    if prediction[0] == -1:
        return "anomaly"

    return "normal"