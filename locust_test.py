from locust import HttpLocust , TaskSet , task , seq_task
import shutil, time
import requests as rq
import random
fit_url = "https://cco-fit-uat.lifelabs.com"
lis_url = "http://spwvapiwp101.diaglabs.corp.priv"  # "https://sdwvxldsk513.diaglabs.corp.priv"
token = "eyJhbGciOiJSUzI1NiIsImtpZCI6IjJhMTU0OTE1M2NjYzFiNmZkMWI3ZjgxZGQ2ZmQ4MGY5IiwidHlwIjoiSldUIn0.eyJuYmYiOjE1NDY0NDM3NzcsImV4cCI6MTU0NjQ1MDk3NywiaXNzIjoiaHR0cHM6Ly9zZHd2eGxkc2s1MTMuZGlhZ2xhYnMuY29ycC5wcml2OjgwOTUiLCJhdWQiOlsiaHR0cHM6Ly9zZHd2eGxkc2s1MTMuZGlhZ2xhYnMuY29ycC5wcml2OjgwOTUvcmVzb3VyY2VzIiwicHd0YXBpIl0sImNsaWVudF9pZCI6InB3dCIsInNjb3BlIjpbInB3dGFwaSJdfQ.xmlA-zY6UMIojfUsKpO7UcmGVuB8e419_hNpfsjwm6vQMruFx8vXwJ1wcyG9clYDLw5vuhT9snraBdGM2w9h7qgQixgsN8IlwFREBdpMn_xIXn5zmTWZEf3F5MYXED0U2jNJwJtyhnG79MwGmktqECN-xmVT2Yipi4AN2L2C1rxmitficO2pPe18T4LmYoOnUK6adI8S80sAKkMQLvMqTOSWmpHd4jwlASKK626v4cvtUR86RTYXya1i7mCAoy-YmOGt4CO4LrfebX5lslhmWt1uCeWzPO3qFm6SUBSjQL4sQ43I523gEx2rbT4dHzHJQl1HBCdtbjTj2LU6Sre9AQ"

class MyTaskSet(TaskSet):
    @task
    def get_patient(hc):
        hc='1015447558'
        a = rq.get(lis_url + "/api/v2/FromCCOFitSrv/patients?hcn="+str(hc)+"&hcnVersion=AA",
                   headers={'Content-Type': 'application/json',
                            'Authorization': "Anything"})

        print (a.text)
        #print(a.status_code)

    def get_provider(id):
        id=random.randint(11111,999999)
        a = rq.get(lis_url + "/api/v2/FromCCOFitSrv/ccofit/providers?search=" + str(id) + "&type=BillingNumber" ,
                   # type=LastName" ,/api/v2/FromCCOFitSrv
                   headers={'Content-Type': 'application/json',
                            'Authorization': "Anything"})

        print(a.status_code)





class MyLocust(HttpLocust):
    task_set = MyTaskSet
    min_wait = 3000
    max_wait = 5000
    host = "http://localhost:8081"

#locust -f C:\Users\patelvi\PycharmProjects\NCE\locust_test.py