from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse,JsonResponse
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer
from .models import com_order_mapper
from .serializers import ComOrderSerializer,ReserveReqSerializer,FulfillmentHoldReleaseReqSerializer,ProvCompleteSerializer
from sol.responseTemplates.reserveResponse import reserveResponse
from sol.responseTemplates.fulfillmentHoldReleaseResp import FulfillmentHoldReleaseresponse
from rest_framework.response import Response
from sol.operations.PendingSubCheck import PendingSubCheck
from sol.operations.GetFELineStatus import GetFELineStatus
from sol.operations.ProvCompleteOPLStatusSyncback import *





# Create your views here.
class ReserveSubscription(APIView):
    def post(self,request):
        serializer=ReserveReqSerializer(data=request.data)
        if serializer.is_valid():
            resp=reserveResponse(serializer.data["salesOrderNo"],serializer.data["offerName"])
            return Response(resp,status=200)
        return Response(serializer.errors,status=400)

class FulfillmentHoldRelease(APIView):
    def post(self,request):
        serializer=FulfillmentHoldReleaseReqSerializer(data=request.data)
        if serializer.is_valid():
            if PendingSubCheck(serializer.data['subRefId'])==True:
                com_order_mapper.objects.create(salesOrderNo=serializer.data['salesOrderNo'],offerName=serializer.data['offerName'],
                                                initialTerm=serializer.data['initialTerm'],
                                                autoRenewalFlag=serializer.data['autoRenewalFlag'],
                                                tfEligible=serializer.data['tfEligible'],subRefId=serializer.data['subRefId'],
                                                deliveryMethod=serializer.data['deliveryMethod'],
                                                subscriptionId=serializer.data['subscriptionId'],quantity=serializer.data['quantity'],
                                                requestedStartDate=serializer.data['requestedStartDate'],prov_email=serializer.data['prov_email'])
                resp=FulfillmentHoldReleaseresponse(serializer.data['salesOrderNo'],serializer.data['offerName'],
                                                    serializer.data['subRefId'],serializer.data['subscriptionId'])

                GetFELineStatus(serializer.data['salesOrderNo'],serializer.data['deliveryMethod'])
                return Response(resp,status=200)
            else:
                return Response({"Status":"FAILURE","Message":"Order already exists for {}".format(serializer.data['subRefId'])})
        return Response(serializer.errors,status=400)

class ProvisioningCompleteView(APIView):
    def post(self,request):
        ser=ProvCompleteSerializer(data=request.data)
        if ser.is_valid():
            com_order_mapper.objects.filter(salesOrderNo=ser.data['salesOrderNo']).update(lineStatus='20')
            ProvCompleteOPLStatusSync(StatusSyncSol(ser.data['salesOrderNo']))

            return Response(ser.data,status=200)
        return Response(ser.errors,status=400)

    pass
@csrf_exempt
@api_view(['GET','POST'])
def solOrderDetails(request):
    if request.method=='GET':
        orders=com_order_mapper.objects.all()
        serializer= ComOrderSerializer(orders,many=True)
        return JsonResponse(serializer.data,safe=False)
    if request.method=='POST':
        data=JSONParser().parse(request)
        serializer=ComOrderSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            return JsonResponse({"Status":"Created Successfully"},status=201)
        return JsonResponse(serializer.errors,status=400)









