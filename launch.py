from flask import Flask, render_template, request, jsonify
from utils import nettoyage, getTrainFromCsv, initVectorizer, predictSentiments
import json

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html", title='Home')

<<<<<<< HEAD
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
=======
@app.route("/result",methods=['POST'])
def retour():
    user_text = request.form.get('input_text')
    print(user_text)
    return json.dumps({'text_user':user_text})

@app.route("/predict",methods=['POST'])
def predict():
    user_text = request.form.get('input_text')
    predictResult = predictSentiments(str(user_text))
    if((predictResult[0][0]) == 1.0):
        strAvis = "Avis Positif"
    else:
        strAvis = "Avis Négatif"

    return jsonify({'text_user':user_text, 'Résultat': strAvis, 'pourcentage de fiabilité': (predictResult[1]*100) })

@app.route("/training",methods=['GET'])
def train():
    #recupere corpus depuis csv
    Corpus = getTrainFromCsv("corpus.csv")
    #nettoie le corpus 
    Corpus['review_net']=Corpus['review'].apply(nettoyage)
    #nettoie le corpus
    #Corpus = nettoyage(Corpus)
    #vectorizer 
    coefFiabilite = initVectorizer(Corpus)
    print(coefFiabilite)
    return jsonify({'Fiabilité de la machine': str(coefFiabilite)})
>>>>>>> d26a2ca0ee094f3a36e42c60923b52d6f8252437


@app.route("/test",methods=['POST'])
def test():
    user_text = request.form.get('input_text')
    print(user_text)
    return json.dumps({'text_user':user_text})


if __name__ == "__main__":
    app.run()