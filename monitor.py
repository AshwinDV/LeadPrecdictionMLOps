from basic_imports import *
import smtplib
from email.message import EmailMessage

#Load train data
train_distribution = pd.read_csv('train_distribution.csv')
landing_page_id = pd.read_csv('landing_page_id_list.csv')
origin = pd.read_csv('origin_list.csv')
logs = pd.read_csv("log.csv", sep=',',header =None,names=['id','origin','pred'])

def sendMail(data):
	msg = EmailMessage()
	msg.set_content(data)
	msg['Subject'] = f'Lead prediction model drift detected'
	msg['From'] = 'botrestaurantsearch@gmail.com'
	msg['To'] = 'ashwindv75@gmail.com'
	# Send the message via our own SMTP server.
	s = smtplib.SMTP('smtp.gmail.com', 587)
	s.starttls()
	s.login('botrestaurantsearch@gmail.com','1234bot%')
	s.send_message(msg)
	s.quit()
		    
def distAnalyisis(logs,train_distribution):
	psi = 0.1
	if psi > .2:
		sendMail('Change in data distibution in detected')
		
	
def metricAnalysis(logs):
	recall = 65
	if recall < 65:
		sendMail('Model performance has degraged')
		
def dataDrift(logs, landing_page_id, origin):
	landing_page_id = list(landing_page_id.iloc[:,0])
	origin = list(origin.iloc[:,0])
	
	for log in logs.iterrows():
		current_landing_page_id = pd.DataFrame(log[1]).iloc[0,0]
		current_origin = pd.DataFrame(log[1]).iloc[1,0]
		
		if current_origin not in origin:
			sendMail('New origin detected')
			
		if current_landing_page_id not in landing_page_id:
			sendMail('New landing page detected')
			
distAnalyisis(logs,train_distribution)
metricAnalysis(logs)
dataDrift(logs, landing_page_id, origin)
	



	
	