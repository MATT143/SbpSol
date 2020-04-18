import os
os.environ['DJANGO_SETTINGS_MODULE'] = 'SbpSol.settings'
import django
django.setup()

from sol.models import com_order_mapper
from django.db.models import Q
from sol.operations.InvokeProvisioning import InvokeProvisioning

def GetPendingProvisioningOrders():
    PendingProvAll=com_order_mapper.objects.filter(Q(lineStatus='32') | Q(lineStatus='11'))
    return PendingProvAll

def MakeInvokeProvReqPayload(i):
    payload={
        'salesOrderNo': i.salesOrderNo,
        'offerName': i.offerName,
        'subRefId': i.subRefId,
        'subscriptionId': i.subscriptionId,
        'deliveryMethod': i.deliveryMethod,
        'prov_email': i.prov_email,
        'quantity': i.quantity
    }
    return payload

def InvokeProvScheduler(req):
    resp=InvokeProvisioning(req)
    return resp


if __name__ == "__main__":
    OrdersInFE=GetPendingProvisioningOrders()
    try:
        for i in OrdersInFE:
            reqPayload=MakeInvokeProvReqPayload(i)
            InvokeProvScheduler(reqPayload)
        print("{'Invoke Provisioning Status':'SUCCESS'}")
    except Exception as e:
        print("{'Invoke Provisioning Status':'FAILURE'}")
        print(e)

