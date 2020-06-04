import requests

data = {
"mql_id":'dac32acd4db4c29c230538b72f8dd87d',
"first_contact_date":'2018-02-01',
"landing_page_id":'88740e65d5d6b056e0cda098e1ea6313',
"origin":'social123'
}

r = requests.post("http://localhost:8000/api/leadpred",json=data)

if r.status_code == 200:
    print(f"Prediction: {r.text}")
else:
    print(f"Failure: {r.text}")