from basic_imports import *

#Read leads data
leads = pd.read_csv('datasets_78342_179673_olist_marketing_qualified_leads_dataset.csv')
closed = pd.read_csv('datasets_78342_179673_olist_closed_deals_dataset.csv')

#Fill origin as unknown if its missing in data
leads['origin'] = leads['origin'].fillna('unknown')
#Drop contact date as there is no seasonality 
leads.drop('first_contact_date', axis=1, inplace = True)

#Select minim required columns 
#mql_id for merging and seller_id to detect if lead was connverted
closed = closed[['mql_id', 'seller_id']]

#Merge data sets
data = pd.merge(leads,closed, how='left', on='mql_id')

#Prepare seller_id as target variable 
data['seller_id'] = data['seller_id'].fillna(0)
data['seller_id'] = data['seller_id'].apply(lambda x: 1 if x else 0)

# Data distribution
dist = data.groupby(['landing_page_id', 'origin'],  as_index=False).mql_id.count()
dist.to_csv (r'train_distribution.csv', index = False, header=True)

landing_page_id_list = pd.DataFrame(data.landing_page_id.unique())
landing_page_id_list.to_csv (r'landing_page_id_list.csv', index = False, header=True)

origin_list = pd.DataFrame(data.origin.unique())
origin_list.to_csv (r'origin_list.csv', index = False, header=True)

#Encode categorical variables for processing in sklearn
with mlflow.start_run():
    encoder_landing_page_id = preprocessing.LabelEncoder()
    encoder_landing_page_id.fit(data['landing_page_id'])
    data['landing_page_id'] = encoder_landing_page_id.transform(data['landing_page_id'])

    encoder_origin = preprocessing.LabelEncoder()
    encoder_origin.fit(data['origin'])
    data['origin'] = encoder_origin.transform(data['origin'])
    
    # Log encoder model to MLflow    
    mlflow.set_tag('Stage', 'Data preporcessing') 
    mlflow.sklearn.log_model(encoder_landing_page_id, "encoder_landing_page_id")
    mlflow.sklearn.log_model(encoder_origin, "encoder_origin")
    mlflow.log_artifact('train_distribution.csv')
    mlflow.log_artifact('landing_page_id_list.csv')
    mlflow.log_artifact('origin_list.csv')

#Separate features and target columns
X = data[['landing_page_id', 'origin']]
y = data['seller_id']

# Splitting the data into train and validation set
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.30, random_state=101)

#Save all data
X_train.to_csv (r'X_train.csv', index = False, header=True)
y_train.to_csv (r'y_train.csv', index = False, header=True)
X_test.to_csv (r'X_test.csv', index = False, header=True)
y_test.to_csv (r'y_test.csv', index = False, header=True)
X.to_csv (r'X.csv', index = False, header=True)
y.to_csv (r'y.csv', index = False, header=True)