
import json,requests


def InvokeProvisioning(req):
    class DatetimeEncoder(
        json.JSONEncoder):  # this class is meant to serialize the date time to json format otherwise json.dumps will fail
        def default(self, obj):
            try:
                return super(DatetimeEncoder, obj).default(obj)
            except TypeError:
                return str(obj)
    reqs = json.dumps(req, cls=DatetimeEncoder)

    invoke_url='http://localhost:9000/sfl/invoke/provisioning'

    response=requests.post(url=invoke_url,data=reqs,headers={'Content-type': 'application/json'})
    return response.json()
