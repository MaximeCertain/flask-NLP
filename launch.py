from flask import Flask, render_template, request
from utils import nettoyage
import json

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html", title='Home')

@app.route("/result",methods=['POST'])
def retour():
    user_text = request.form.get('input_text')
    print(user_text)
    return json.dumps({'text_user':user_text})

@app.route("/prediction",methods=['GET'])
def predict():
    predicts = "c'est nul denis c'est nul de A à Z c'est zéro"
    predicts = nettoyage(predicts)
    print(predicts)
    #user_text = request.form.get('input_text')
    #print(user_text)
    #utiliser la prédiction

    return "ooooookkkkk"

if __name__ == "__main__":
    app.run()

