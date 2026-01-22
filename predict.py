import pickle
import numpy as np


with open('model/wine_model.pkl', 'rb') as f:
    model = pickle.load(f)


cultivators = {
    0: "Cultivator 1",
    1: "Cultivator 2",
    2: "Cultivator 3"
}


def predict_wine(features):
    features = np.array(features).reshape(1, -1)
    prediction = model.predict(features)[0]
    return cultivators[prediction]