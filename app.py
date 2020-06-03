from basic_imports import *
from flask import Flask, request, jsonify
import numpy as np  
from tensorflow.keras.models import load_model
import joblib

def return_prediction(model,en1,en2,sample_json):
    
    #Extract features
    landing_page_id = sample_json['landing_page_id']
    origin = sample_json['origin']
    
    landing_page_id_en = en1.transform(pd.DataFrame([landing_page_id]))
    origin_en = en2.transform(pd.DataFrame([origin]))
    
    data = pd.DataFrame([[landing_page_id_en[0],origin_en[0]]])
    classes = np.array(['Potential Conversion', 'Unlikely Conversion'])
    
    class_ind = model.predict(data)
    
    with open('log.csv', 'a') as out:
    	out.write(str(landing_page_id)+','+str(origin)+','+str(class_ind[0])+'\n')
    
    return classes[class_ind][0]


app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Lead conversion prediction app</h1>'


# Load encoders
encoder_landing_page_id = mlflow.sklearn.load_model('mlruns/0/4991cca94fbc4a3fb2ead6fac8ae8d6b/artifacts/encoder_landing_page_id')
encoder_origin = mlflow.sklearn.load_model('mlruns/0/4991cca94fbc4a3fb2ead6fac8ae8d6b/artifacts/encoder_origin')

# Load model
model = model = mlflow.sklearn.load_model('mlruns/0/dbade588f1f44c5db2427ae03ad95ad5/artifacts/RandonForest')

@app.route('/api/leadpred', methods=['POST'])
def predict_flower():

    content = request.json
    results = return_prediction(model=model, en1=encoder_landing_page_id, en2=encoder_origin, sample_json=content)
    
    return jsonify(results)

if __name__ == '__main__':
    app.run()