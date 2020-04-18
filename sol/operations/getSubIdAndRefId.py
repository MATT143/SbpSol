from random import randint


def getSubscriptionId():
    num = randint(10000, 99999)
    subscriptionId = 'SubC' + str(num)
    return subscriptionId


def getSubRefId():
    num = randint(10000, 99999)
    subRefId = 'Sub' + str(num)
    return subRefId





