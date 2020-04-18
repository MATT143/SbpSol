from rest_framework import serializers
from .models import com_order_mapper
from .requestTemplates.reserveRequest import reserveSubRequest
from .requestTemplates.fulfillmentHoldreleaseRequest import FulfillmentHoldreleaseRequest
from .requestTemplates.ProvCompleteCallbackRequest import ProvCompleteCallBackRequest


class ComOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model=com_order_mapper
        fields='__all__'

class ReserveReqSerializer(serializers.Serializer):
    salesOrderNo=serializers.CharField(max_length=20)
    offerName=serializers.CharField(max_length=50)
    def create(self, validated_data):
        return reserveSubRequest(validated_data)

# class FulfillmentHoldReleaseReqSerializer(serializers.Serializer):
#     salesOrderNo = serializers.CharField(max_length=20)
#     offerName = serializers.CharField(max_length=20)
#     initialTerm = serializers.IntegerField()
#     autoRenewalFlag = serializers.BooleanField()
#     tfEligible = serializers.BooleanField()
#     subRefId = serializers.CharField(max_length=20)
#     subscriptionId = serializers.CharField(max_length=20)
#
#     def create(self, validated_data):
#         return FulfillmentHoldreleaseRequest(validated_data)

class FulfillmentHoldReleaseReqSerializer(serializers.ModelSerializer):
    class Meta:
        model=com_order_mapper
        exclude=['lineStatus','creationDate']


class ProvCompleteSerializer(serializers.Serializer):
    salesOrderNo = serializers.CharField(max_length=20)
    lineStatus=serializers.CharField(max_length=10)
    def create(self, validated_data):
         return ProvCompleteCallBackRequest(validated_data)









