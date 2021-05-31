import os
import numpy as np
import tensorflow as tf 

from tensorflow.keras.applications.inception_v3 import preprocess_input 
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image 

from flask import Flask, redirect, url_for, request, render_template
from werkzeug.utils import secure_filename

app = Flask(__name__)

MODEL_PATH = r"C:\Users\jgaur\End_To_End_Projects(DL)\Cotton_Disease\model.h5"

model = load_model(MODEL_PATH)

def model_predict(img_path, model):
    print(img_path)
    img = image.load_img(img_path, target_size=(224, 224))

    x = image.img_to_array(img)
    x = x / 255
    x = np.expand_dims(x, axis=0)

    # x = preprocess_input(x)
    preds = model.predict(x)
    preds
    preds = np.argmax(preds, axis=1)
    print(preds)

    if preds == 0:
        preds = "The leaf is diseased cotton leaf"
    elif preds == 1:
        preds = "The leaf is diseased cotton plant"
    elif preds == 2:
        preds = "The leaf is fresh cotton leaf"
    elif preds == 3:
        preds = "The leaf is fresh cotton plant"

    return preds

    

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/predict', methods=['GET', 'POST'])
def uplaod():
    if request.method == 'POST':
        f = request.files['file']

        basepath = os.path.dirname(__file__)
        print()
        print(basepath)
        print()
        file_path = os.path.join(basepath, 'uploads', secure_filename(f.filename))
        f.save(file_path)

        preds = model_predict(file_path, model)
        result = preds
        return result
    return None 

if __name__ == '__main__':
    app.run(debug=True)