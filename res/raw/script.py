import android, time
droid = android.Android()

res=droid.getConstants("android.provider.ContactsContract$CommonDataKinds$Phone").result

uri = res['CONTENT_URI']


spokenMessageIds=[]

while True:
	time.sleep(1)
	for message in droid.smsGetMessages(True, 'inbox', None ).result:
		messageId = message['_id']
		if  messageId not in spokenMessageIds:	
		
			number = message['address']	
			
			#Matching number from message
			filter = "data1='"+number[3:]+"' OR data1='"+number+"'"
			
			if len(number)>=8:
				broken1 = number[0:3]+" "+number[3:5]+" "+number[5:7]+" "+number[7:] #+91 98 19 379097
				broken2 = number[3:5]+" "+number[5:7]+" "+number[7:]                 #98 19 379097
				filter=filter + " OR data1='"+broken1+"' OR data1='"+broken2+"'"
			
			#Query phone database for getting name
			matches = droid.queryContent(uri,['display_name','data1'],filter,None,None).result 
			
			print 'number of mathches=',len(matches)
			
			if len(matches)!=0:     #If Name of number found
				contact=matches[0]  #Select First contact
				print "Matches found=",matches
				print "selected match=",contact
				say = 'Message from ' + contact['display_name']
				droid.ttsSpeak(say)
				spokenMessageIds.append(messageId)
			
	
	
