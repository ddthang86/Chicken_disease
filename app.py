# Import required modules and libraries
from flask import Flask, request, jsonify, render_template
import os
from flask_cors import CORS, cross_origin
from cnnClassifier.utils.common import decodeImage
from cnnClassifier.pipeline.predict import PredictionPipeline

# Set environment variables to handle Unicode encoding
os.putenv('LANG', 'en_US.UTF-8')
os.putenv('LC_ALL', 'en_US.UTF-8')

# Create a Flask application and enable Cross-Origin Resource Sharing (CORS)
app = Flask(__name__)
CORS(app)

# ClientApp class to manage the filename and PredictionPipeline object
class ClientApp:
    def __init__(self):
        self.filename = "inputImage.jpg"
        self.classifier = PredictionPipeline(self.filename)

# Define the route for the home page
@app.route("/", methods=['GET'])
@cross_origin()
def home():
    return render_template('index.html')

# Define the route for training the model
@app.route("/train", methods=['GET', 'POST'])
@cross_origin()
def trainRoute():
    os.system("python main.py")  # Execute the 'main.py' script for training
    return "Training done successfully!"

# Define the route for predicting using the model
@app.route("/predict", methods=['POST'])
@cross_origin()
def predictRoute():
    image = request.json['image']  # Get the image data from the request
    decodeImage(image, clApp.filename)  # Decode the image data and save to 'inputImage.jpg'
    result = clApp.classifier.predict()  # Use the PredictionPipeline to predict the image
    return jsonify(result)  # Return the prediction result in JSON format

# Main block to create the ClientApp object and run the Flask application
if __name__ == "__main__":
    clApp = ClientApp()  # Create a ClientApp object to manage the prediction pipeline
    # app.run(host='0.0.0.0', port=8080) # Run the app on local host (commented out)
    app.run(host='0.0.0.0', port=8080) # Run the app on AWS (commented out)
    # app.run(host='0.0.0.0', port=80)  # Run the app on Azure
