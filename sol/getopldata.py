import requests
import json
oplurl = "http://localhost:8080/opl/"
solurl=" http://localhost:5000/sol/"


def fetchOplData():
    resp = requests.get(url=oplurl, headers={'content-type': 'application/json'})
    OplResponse = resp.json()
    return OplResponse


def PublishInSol(oplResponse):
    for object in oplResponse:
        subRefId = object['subRefId']
        salesOrderNo = object['webOrderId']
        offerName = object['Offer']
        SolRequest = {"subRefId": subRefId, "salesOrderNo": salesOrderNo, "offerName": offerName}
        solResp = requests.post(url=solurl, data=json.dumps(SolRequest),headers={'Content-type': 'application/json'})
    return solResp.json()

if __name__=="__main__":
    PublishInSol(fetchOplData())

