from sol.models import com_order_mapper


def GetFELineStatus(salesOrderNo,deliveryMethod):
    if deliveryMethod=='CLOUD':
        com_order_mapper.objects.filter(salesOrderNo=salesOrderNo).update(lineStatus='32')
    else:
        com_order_mapper.objects.filter(salesOrderNo=salesOrderNo).update(lineStatus='11')

    return True

