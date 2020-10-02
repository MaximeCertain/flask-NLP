
import re
from unidecode import unidecode
from nltk.stem import SnowballStemmer
from nltk.corpus import stopwords
from stop_words import get_stop_words
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split

#get les stop words langues FR 
def getStopWords():
    fr = SnowballStemmer('french')
    my_stop_word_list = get_stop_words('french')
    final_stopwords_list = stopwords.words('french')
    s_w=list(set(final_stopwords_list+my_stop_word_list)) #concatene les deux listes de stop words
    s_w=[elem.lower() for elem in s_w]
    return s_w

#fonction de nettoyage d'une chaine de characteres
def nettoyage(string):
    l=[]
    string=unidecode(string.lower()) #enleve acccent et passe la chaine en miniscule
    #Sans ponctuation pour le moment
    string=" ".join(re.findall("[a-zA-Z]+", string))  #joint les tuples dans une chaine avec un separateur, ne l'applique que sur ceux qui respecte le regex
    stopwords = getStopWords()
    for word in string.split():
        if word in stopwords:  #si mot dans les stopwords, il n'est pas validé
            continue
        else:  #si mot pas dans les stopwords alors on l'jaoute à la la liste des mots
            #l.append(fr.stem(word))
            l.append(word)
    return ' '.join(l)  #reforme la string en séparant les mots par des espaces 


def initVectorizer(corpus):
    vectorizer = TfidfVectorizer()  #initialise matrice tf idf 
    vectorizer.fit(Corpus['review_net']) #met en forme le vectorizer avec la nvlle colonne cleanée
    X=vectorizer.transform(Corpus['review_net'])
    pickle.dump(vectorizer.vocabulary_,open("feature.pkl","wb")) #enregistre les mots dans un fichier pickle


def predictSentiements():
    return 1