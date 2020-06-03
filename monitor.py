from basic_imports import *

#Load train data
train_distribution = pd.read_csv('train_distribution.csv')
landing_page_id_list = pd.read_csv('landing_page_id_list.csv')
origin_list = pd.read_csv('origin_list.csv')
logs = pd.read_csv("log.csv", sep=',',header =None,names=['id','origin','pred'])
print(logs.head())