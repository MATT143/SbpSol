
from sol.operations.getSubIdAndRefId import getSubRefId,getSubscriptionId
from sol.operations.CheckExistingSub import checkExistingSub
from sol.models import com_order_mapper
import json


def reserveResponse(salesOrderNo,offerName):
    subId = getSubscriptionId()
    SubRefId = getSubRefId()
    result = checkExistingSub(subId, SubRefId)
    while result==False:
        subId=getSubscriptionId()
        SubRefId=getSubRefId()
        result=checkExistingSub(subId,SubRefId)
    response={"salesOrderNo":salesOrderNo,"offerName":offerName,"subscriptionId":subId,"subRefId":SubRefId}
    return response


class reserveSubResponse(object):
    def __init__(self,salesOrderNo,offerName,subscriptionId,subRefId):
        self.salesOrderNo=salesOrderNo
        self.offerName=offerName
        self.subscriptionId=subscriptionId
        self.subRefId=subRefId
