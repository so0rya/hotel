from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from hotel.models import Dishes
from hotel.serializer import DishSerializer

class DishesView(APIView):
    def get(self,request,*args,**kwargs):
        all_dishes=Dishes.objects.all()
        serializer=DishSerializer(all_dishes,many=True)
        return Response(data=serializer.data)
    def post(self,request,*args,**kwargs):
        serializer=DishSerializer(data=request.data)
        if serializer.is_valid():
            name=serializer.validated_data.get("name")
            category=serializer.validated_data.get("category")
            price=serializer.validated_data.get("price")
            Dishes.objects.create(name=name
                                  ,price=price,category=category)
            return Response(data=serializer.data)
        else:
            return Response(data=serializer.errors)

class DishDetailsView(APIView):
    def get(self,request,*args,**kwargs):
        id=kwargs.get("id")
        dish=Dishes.objects.get(id=id)
        serializer=DishSerializer(dish)
        return Response(data=serializer.data)
    def delete(self,request, *args, ** kwargs):
        id = kwargs.get("id")
        dish = Dishes.objects.get(id=id)
        dish.delete()
        return Response({"msg":"deleted"})