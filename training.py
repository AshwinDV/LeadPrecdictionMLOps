from basic_imports import *

#Load entire data
X = pd.read_csv('X.csv')
y = pd.read_csv('y.csv')

#Handle class imbalance
sm = SMOTE(random_state = 2) 
X_res, y_res = sm.fit_sample(X, y.values.ravel())

#Initialise with chosen parameters 
rfc = RandomForestClassifier(min_samples_split=2, n_estimators=50, random_state=42)
# fit
rfc.fit(X_res,y_res)

#Compute tran data accuracy for reference
predictions = rfc.predict(X_res)

#Log values
with mlflow.start_run():
    mlflow.set_tag('Stage', 'Training') 
    mlflow.log_param("min_samples_split", 2)
    mlflow.log_param("n_estimators", 50)
    mlflow.sklearn.log_model(rfc, "RandonForest")
    mlflow.log_metric("recall", classification_report(y_res,predictions,output_dict=True)['1']['recall'])
    mlflow.log_metric("precision", classification_report(y_res,predictions,output_dict=True)['1']['precision'])