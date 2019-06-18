import sys 
import json
import pandas as pd
import numpy as np
import pickle
from http.server import BaseHTTPRequestHandler, HTTPServer

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

class ML_RequestHandler(BaseHTTPRequestHandler):
    def predict(self, image):
        prediction = MODEL.predict(np.asarray([image]).astype('u8'))
        return bool(prediction[0])
    
    def do_POST(self):
        content_len = int(self.headers.get('Content-Length'))
        post_body = self.rfile.read(content_len)
        image = json.loads(post_body)
        prediction = json.dumps({"is_trousers": self.predict(image)})
        print(prediction)
        
        # Send response status code
        self.send_response(200)
 
        # Send headers
        self.send_header('Content-type','application/json')
        self.end_headers()
 
        # Send message back to client
        # Write content as utf-8 data
        self.wfile.write(bytes(prediction, "utf8"))
        return
    
def run_server():
    print('starting server...')
 
    server_address = ('127.0.0.1', 8001)
    httpd = HTTPServer(server_address, ML_RequestHandler)
    print('running server...')
    httpd.serve_forever()


try:
    restore_model()  # The first time that this script is run, the model will be created and cached. Thereafter it is reused.
except:
    create_and_persist_model()



if __name__ == '__main__':
    run_server()