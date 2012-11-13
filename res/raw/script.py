import android, time
droid = android.Android()

allcontacts = droid.contactsGet(None).result

spokenMessageIds=[]

while True:
	time.sleep(1)
	for messsage in droid.smsGetMessages(True, 'inbox', None ):
		messageId = message['_id']
		if  messageId not in spokenMessageIds:	
			number = message['address']	
			for contact in allcontacts:
				if number is contact['number']:
					say = 'Message from ' + contact['name']
					droid.ttsSpeak(say)
					spokenMessageIds.append(messageId)
			
	
	
