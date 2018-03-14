from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import mixins
from rest_framework import generics

from .models import Goods
from .serializers import GoodsSerializer
# Create your views here.


class GoodsListView(generics.ListAPIView):
    """
    all of goods
    """
    # def get(self, request, format=None):
    #     goods = Goods.objects.all()[:10]
    #     goods_serializer = GoodsSerializer(goods, many=True)
    #     return Response(goods_serializer.data)

    queryset = Goods.objects.all()
    serializer_class = GoodsSerializer