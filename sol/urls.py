from django.urls import path
from .views import solOrderDetails,ReserveSubscription,FulfillmentHoldRelease,ProvisioningCompleteView

urlpatterns = [
    path('sol/',solOrderDetails),
    path('sol/reserve/subscription',ReserveSubscription.as_view()),
    path('sol/fulfillment/holdrelease',FulfillmentHoldRelease.as_view()),
    path('sol/provision/complete',ProvisioningCompleteView.as_view())

]
