from flask import Flask, render_template, request
from utils import nettoyage
import json

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html", title='Home')

@app.route("/yo",methods=['POST'])
def predict():
    user_text = request.form.get('input_text')
    predicts = "c'est nul denis c'est nul de A à Z c'est zéro"
    
    print(predicts)
    #user_text = request.form.get('input_text')
    #print(user_text)
    #utiliser la prédiction

    return render_template("prediction.html", title='Prediction', input_text = user_text, message = predicts)

@app.route("/training3",methods=['GET'])
def training():
    return render_template("training.html", title='Training')

if __name__ == "__main__":
    app.run()

