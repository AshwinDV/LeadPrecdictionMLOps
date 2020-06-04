from basic_imports import *

#Load data
X_train = pd.read_csv('X_train.csv')
y_train = pd.read_csv('y_train.csv')
X_test = pd.read_csv('X_test.csv')
y_test = pd.read_csv('y_test.csv')

#Handle class imbalance
sm = SMOTE(random_state = 2) 
X_train_res, y_train_res = sm.fit_sample(X_train, y_train.values.ravel())

#Initialise with best possible parameters
rfc = RandomForestClassifier(min_samples_split=2, n_estimators=50, random_state=42)
# fit
rfc.fit(X_train_res,y_train_res)

#Validate model on unseen data
predictions = rfc.predict(X_test)

#Log values
with mlflow.start_run():
    mlflow.set_tag('Stage', 'Validation') 
    mlflow.log_param("min_samples_split", 2)
    mlflow.log_param("n_estimators", 50)
    mlflow.sklearn.log_model(rfc, "RandonForest")
    mlflow.log_metric("recall", classification_report(y_test,predictions,output_dict=True)['1']['recall'])
    mlflow.log_metric("precision", classification_report(y_test,predictions,output_dict=True)['1']['precision'])