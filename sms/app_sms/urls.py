from django.urls import path
from .views import Send_SMS
urlpatterns = [
    path('', Send_SMS.as_view(), name='sms'),
]