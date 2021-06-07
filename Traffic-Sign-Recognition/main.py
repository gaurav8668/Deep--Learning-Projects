from flask import Flask, render_template, url_for, request
import tensorflow as tf 
from tensorflow.keras.models import load_model 
from PIL import Image 
import numpy as np

model = load_model('R_G_B_model.h5')

def predict(img):
    img = Image.open(img)
    img = img.resize((32, 32))
    img = np.array(img)
    img = img/255.0
    print(img.shape)
    img = np.expand_dims(img, axis=0)
    print(img.shape)
    pred = model.predict(img)
    print(pred)
    pred = np.argmax(pred, axis=-1)
    print(pred)
    return pred

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/about', methods=['GET'])
def about():
    return render_template('about.html')

@app.route('/predictor', methods=['GET', 'POST'])
def predictor():
    if request.method == 'POST':
        img_path = request.files['file']
        if img_path == None:
            return render_template('predictor.html', result="Please choose valid path")
        else:
            pred = predict(img_path)
            x = int(pred)
            if x == 0:
                x = 'Speed limit (20km/h)'
            elif x == 1:
                x = 'Speed limit (30km/h)'
            elif x == 2:
                x = 'Speed limit (50km/h)'
            elif x == 3:
                x = 'Speed limit (60km/h)'
            elif x == 4:
                x = 'Speed limit (70km/h)'
            elif x == 5:
                x = 'Speed limit (80km/h)'
            elif x == 6:
                x = 'Speed limit (80km/h)'
            elif x == 7:
                x = 'Speed limit (100km/h)'
            elif x == 8:
                x = 'Speed limit (120km/h)'
            elif x == 9:
                x = 'No passing'
            elif x == 10:
                x = 'No passing veh over 3.5 tons'
            elif x == 11:
                x = 'Right-of-way at intersection'
            elif x == 12:
                x = 'Priority road'
            elif x == 13:
                x = 'Yield'
            elif x == 14:
                x = 'Stop'
            elif x == 15:
                x = 'No vehicles'
            elif x == 16:
                x = 'Veh > 3.5 tons prohibited'
            elif x == 17:
                x = 'No vehicles'
            elif x == 18:
                x = 'General caution'
            elif x == 19:
                x = 'Dangerous curve left'
            elif x == 20:
                x = 'Dangerous curve right'
            elif x == 21:
                x = 'Double curve'
            elif x == 22:
                x = 'Bumpy road'
            elif x == 23:
                x = 'Slippery road'
            elif x == 24:
                x = 'Road narrows on the right'
            elif x == 25:
                x = 'Road work'
            elif x == 26:
                x = 'Traffic signals'
            elif x == 27:
                x = 'Pedestrians'
            elif x == 28:
                x = 'Children crossing'
            elif x == 29:
                x = 'Bicyles crossing'
            elif x == 30:
                x = 'Beware of ice/snow'
            elif x == 31:
                x = 'Wild animals crossing'
            elif x == 32:
                x = 'End speed + passing limits'
            elif x == 33:
                x = 'Turn right ahead'
            elif x == 34:
                x = 'Turn left ahead'
            elif x == 35:
                x = 'Ahead only'
            elif x == 36:
                x = 'Go straight or right'
            elif x == 37:
                x = 'Go straight or left'
            elif x == 38:
                x = 'Keep right'
            elif x == 39:
                x = 'keep left'
            elif x == 40:
                x = 'Roundabout mandatory'
            elif x == 41:
                x = 'End of no passing'
            elif x == 42:
                x = 'End of no passing veh > 3.5 tons'
            
            return render_template('predictor.html', result=x)
    else:
        return render_template('predictor.html')

if __name__ == '__main__':
    app.run(debug=True)