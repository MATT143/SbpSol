import requests
import json

def StatusSyncSol(i):
    payload={'salesOrderNo':i,'flowStatus':'PROVISION COMPLETE'}
    return payload

def ProvCompleteOPLStatusSync(req):
    url='http://localhost:7000/opl/provcomplete/syncback'
    resp=requests.post(url=url,data=json.dumps(req),headers={'Content-type': 'application/json'})
    return resp.json()