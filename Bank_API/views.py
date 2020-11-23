from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny,IsAuthenticated
from rest_framework.response import Response
from django.core.paginator import Paginator
from .models import Banks,Branches
from .serializer import BankBranchSerializer
from rest_framework import pagination,viewsets
from django.contrib.auth.models import User
# Create your views here.

# class StandardResultsSetPagination(PageNumberPagination):
#     page_size = 100
#     page_size_query_param = 'page_size'
#     max_page_size = 1000

class IfcApi(APIView):
    permission_classes = [IsAuthenticated]
    def get(self,request):

        # str_ifsc = request.data.get('data')
        # query_set = Branches.objects.filter(ifsc = str_ifsc)
        query_set = Branches.objects.all()
        serializer_ = BankBranchSerializer(query_set,many=True)
        return Response({"status":serializer_.data})

class BankApi(APIView):
    def post(self,request):
        str_bank = request.data.get('bank')
        str_city = request.data.get('city')
        int_page = request.data.get("page") or 10
        page_size = request.data.get("page_size") or 10

        query_set = Branches.objects.filter(bank__name = str_bank,city = str_city)
        serializer_ = BankBranchSerializer(query_set,many=True)
        paginator = Paginator(list(serializer_.data), page_size)
        page_obj = paginator.get_page(int_page)
        return Response({"status":page_obj.object_list})

class register(APIView):
    def post(self,request):
        username = request.data['username']
        password = request.data['password']
        name = request.data['name']


        # {"usename":"test1,"password":"test","name":"test"}
        # {"bank":"ABHYUDAYA COOPERATIVE BANK LIMITED","city":"MUMBAI","page":3,"page_size":30}