#import required modules
import numpy as np
import pandas as pd
import datetime
from sklearn import preprocessing
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report,confusion_matrix, accuracy_score
from imblearn.over_sampling import SMOTE 
from sklearn.model_selection import KFold
from sklearn.model_selection import GridSearchCV
import mlflow
import mlflow.sklearn
from mlflow import log_metric, log_param, log_artifact
import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning) 