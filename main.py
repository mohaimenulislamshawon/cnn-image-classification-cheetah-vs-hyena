from flask import Flask, render_template, request
from PIL import Image
import io
import numpy as np
from tensorflow.keras.models import load_model

app = Flask(__name__)

# Load the pre-trained CNN model
model = load_model('model.hdf5')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        # Get the uploaded file
        f = request.files['image']

        # Read image with PIL
        img = Image.open(io.BytesIO(f.read()))
        img = img.resize((200, 200))

        # Convert PIL image to numpy array
        img = np.expand_dims(np.array(img), axis=0) / 255.0

        # Make prediction using the model
        pred = model.predict(img)[0][0]
        pred = round(pred)

        if pred == 1:
            pred_text = "Hyena" 
        else:
            pred_text = "Cheetah"

        return render_template('result.html', prediction=pred_text)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=81)
