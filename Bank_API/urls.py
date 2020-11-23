from django.urls import path
from .views import IfcApi,BankApi,register
urlpatterns = [
    path("",IfcApi.as_view()),
    path("bank/",BankApi.as_view()),
    path("register/",register.as_view()),
]