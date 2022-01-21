from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Stock
from .serializers import StockSerializer

# Create your views here.
class Liststock(APIView):
    def get(self, request):
        stocks = Stock.objects.all() 
        stock_json = StockSerializer(stocks, many=True)
        return Response(stock_json.data)

    def post(self, request):
        stock_json = StockSerializer(data=request.data)
        if stock_json.is_valid():
            stock_json.save()
            return Response(stock_json.data, status=201)
        return Response(stock_json.errors, status=400)

class DetailStock(APIView):
    def get(self, request, pk):
        stock = Stock.objects.get(pk=pk) 
        stock_json = StockSerializer(stock)
        return Response(stock_json.data)