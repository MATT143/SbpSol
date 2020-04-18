
from sol.models import com_order_mapper

def checkExistingSub(subId,subRefId):
    q1 = com_order_mapper.objects.filter(subscriptionId=subId)
    q2=com_order_mapper.objects.filter(subRefId=subRefId)
    if len(q1)==0 and len(q2)==0:
        return True
    return False