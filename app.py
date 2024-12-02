from flask import Flask, request, jsonify, render_template
import os
from flask_cors import CORS, cross_origin
#image given is raw image and it converted to base64 string
from cnnClassifier.utils.common import decodeImage
from src.cnnClassifier.pipeline.prediction import PredictionPipeline
import logging

# Setup logging
logging.basicConfig(level=logging.INFO)

#initialize the flask
os.putenv('LANG', 'en_US.UTF-8')
os.putenv('LC_ALL', 'en_US.UTF-8')

app = Flask(__name__)
CORS(app)

#so whatever image uder pass save ti as input image and filename give to predictionpipeline and this will give classifier object 0/1
class ClientApp:
    def __init__(self):
        self.filename = "inputImage.jpg"
        self.classifier = PredictionPipeline(self.filename)

#create the default route and it return index.html
@app.route("/", methods=['GET'])
@cross_origin()
def home():
    return render_template('index.html')


#then create the train route so user can also trina the model
@app.route("/train", methods=['GET','POST'])
@cross_origin()
def trainRoute():
    os.system("python main.py")
    # os.system("dvc repro")
    return "Training done successfully!"
    # os.system("dvc repro") #if want to track the file aso


#add the preciction route #take image and decode image and save and apply the predict operation
@app.route("/predict", methods=['POST'])
@cross_origin()
def predictRoute():
    try:
        image = request.json['image']
        decodeImage(image, clApp.filename)
        result = clApp.classifier.predict()
        return jsonify(result)
    except Exception as e:
        logging.exception("An error occurred during prediction.")
        return str(e), 500

if __name__ == "__main__":
    clApp = ClientApp()

    app.run(host='0.0.0.0', port=8080) #for AWS
