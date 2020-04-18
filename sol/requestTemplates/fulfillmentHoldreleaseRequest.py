

class FulfillmentHoldreleaseRequest(object):
    def __init__(self, salesOrderNo, offerName,initialTerm,autoRenewalFlag,tfEligible,subRefId,subscriptionId):
        self.salesOrderNo = salesOrderNo
        self.offerName = offerName
        self.initialTerm = initialTerm
        self.autoRenewalFlag = autoRenewalFlag
        self.tfEligible = tfEligible
        self.subRefId = subRefId
        self.subscriptionId=subscriptionId