import requests
#import names
import random
import json


fn = "vick1"#names.get_first_name (gender='male')
ln = "vick1"#names.get_last_name ()
j = str (random.randint (100 , 200))
url = "https://192.168.152.24/rest/jsonp/invoice/public?name=" + fn + "&lastName=" + ln + \
      "&phone=(416)+416-4160&optin=false&store=1219&source=locator&product=6055"

re = requests.get(url,verify=False)
s = (re.content).decode('utf-8')
print(s)
start='"idSnapshot":{"id":'
end='}},"userInfo"'
b= s[s.find(start)+len(start):s.find(end)]
print(b)

cancel_url ="https://192.168.152.24/rest/jsonp/invoice/"+str(b)+"/void/public?name=" + fn + "&lastName=" + ln + \
            "&phone=(416)+416-4160&optin=false&store=1244"

g =requests.get(cancel_url,verify=False)
print(g.content)

'''
s= """
{"objectId":{"entityName":"Invoice","idSnapshot":{"id":286}},"userInfo":{},"active":true,"appointmentTime":null,"customFields":"{\\"emailOptIn\\":false}","estimatedWaitMinutes":10,"externalId":"7930139","iosLastPushedWaitTime":-1,"numberOfCustomers":1,"originalEstWait":10,"source":"locator","timeArrived":null,"timeIn":"2018-11-16T10:44:29.353","timeOut":null,"timeServed":null,"timeVoided":null,"voided":false,"customer":{"objectId":{"entityName":"Customer","idSnapshot":{"id":218}},"userInfo":{},"cookieId":218,"customFields":null,"iosBundleId":null,"iosDeviceToken":null,"store":{"objectId":{"entityName":"Store","idSnapshot":{"id":1219}}},"lastName":"Ratledge","phone":"(416) 416-4160","ipAddress":"10.144.56.84","birthDate":null,"fullName":"Fredrick Ratledge","name":"Fredrick","pkStr":"218"},"details":[{"objectId":{"entityName":"InvoiceDetail","idSnapshot":{"id":146}},"userInfo":{},"deleted":false,"product":{"objectId":{"entityName":"Product","idSnapshot":{"id":6055}},"userInfo":{},"active":true,"defaultServiceTimeMinutes":15,"deleted":false,"name":"Testing","primary":false,"productInfo":null,"waitPadOnly":false,"store":{"objectId":{"entityName":"Store","idSnapshot":{"id":1219}}},"id":6055,"pkStr":"6055"},"pkStr":"146"}],"employee":null,"primaryInvoice":null,"requestedEmployee":null,"store":{"objectId":{"entityName":"Store","idSnapshot":{"id":1219}}},"invoiceDate":"2018-11-16","completed":false,"oci":true,"estimatedRemainingServiceTime":15,"absent":false,"request":false,"pkStr":"286"}'
"""
start='idSnapshot":{"id":'
end='}},"userInfo"'
b= s[s.find(start)+len(start):s.find(end)]
print(b)
'''

"""
for i in range(100):
    r = "https://192.168.152.24/rest/jsonp/product/public?store="+str(1000+i)
    re = requests.get(r,verify=False)
    if len(re.content)>50:
        print(re.content)

"""