from sol.models import com_order_mapper

def PendingSubCheck(SubRefId):
    q1=com_order_mapper.objects.all().filter(subRefId__exact=SubRefId)
    if len(q1)==0:
        return True
    else:
        return False
