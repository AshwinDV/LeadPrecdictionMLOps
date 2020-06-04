from basic_imports import *

#Load train data
X_train = pd.read_csv('X_train.csv')
y_train = pd.read_csv('y_train.csv')

#Handle class imbalance 
sm = SMOTE(random_state = 2) 
X_train_res, y_train_res = sm.fit_sample(X_train, y_train.values.ravel())

# Create the parameter grid based on the results of random search 
param_grid = {
    'min_samples_split': range(2, 10, 2),
    'n_estimators': [10, 50, 100]
}

# Create a base model
rf = RandomForestClassifier(random_state=42)

# Instantiate the grid search model
grid_search = GridSearchCV(estimator = rf, param_grid = param_grid, scoring="recall",
                          cv = 3, n_jobs = -1,verbose = 1)
                          
# Fit the grid search to the data
grid_search.fit(X_train_res, y_train_res)

#Log best values for parameter and associated recall value 
with mlflow.start_run():
    mlflow.set_tag('Stage', 'Hyperparameter Tuning') 
    mlflow.log_params(grid_search.best_params_)
    mlflow.log_metric("recall", grid_search.best_score_)