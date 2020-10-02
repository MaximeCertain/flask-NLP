from flask import Flask, render_template, request, jsonify
from utils import nettoyage, getTrainFromCsv, initVectorizer, predictSentiments
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


@app.route("/test",methods=['POST'])
def test():
    user_text = request.form.get('input_text')
    print(user_text)
    return json.dumps({'text_user':user_text})


if __name__ == "__main__":
    app.run()