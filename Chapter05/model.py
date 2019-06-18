import sys 
import json
import pandas as pd
import numpy as np
import pickle

MODEL = None
MODEL_FILENAME = "model.pickle"

def create_and_persist_model():
    global MODEL
    from keras.datasets import fashion_mnist
    (x, y), _  = fashion_mnist.load_data()
    classes =	['tshirt', 'trouser', 'pullover', 'dress', 'coat', 'sandal', 'shirt', 'shoe', 'bag', 'boot']
    from sklearn.model_selection import train_test_split
    x_train, x_test, y_train, y_test = train_test_split(x[:1000].reshape(-1, 28 * 28), y[:1000].flatten(), test_size=0.25, random_state=0)
    # Prepare examples
    y_train_1 = y_train == 1
    y_test_1 = y_test == 1
    from sklearn.linear_model import LogisticRegression
    MODEL = LogisticRegression(solver='liblinear').fit(x_train, y_train_1)
    pickle.dump(MODEL, open(MODEL_FILENAME, "wb" ))   

def restore_model():
    global MODEL
    MODEL = pickle.load( open( "model.pickle", "rb" ) )

def predict(data):
    """Return a prediction given input"""
    #print(np.asarray([data]).astype('u8'))
    #return
    prediction = MODEL.predict(np.asarray([data]).astype('u8'))
    print('{"error": null, "is_trousers": ' + str(prediction[0]).lower()  + '}')

try:
    restore_model()  # The first time that this script is run, the model will be created and cached. Thereafter it is reused.
except:
    create_and_persist_model()

if len(sys.argv) == 1:
    # Fit model only
    print('{"error": null}')
    sys.exit(0)

if sys.argv[1] == 'predict':
    # Predict
    if len(sys.argv) != 3:
        print('{"error": "incorrect number of arguments"}')
        sys.exit(1)
    d = json.loads(sys.argv[2])
    predict(d)
sys.exit(0)