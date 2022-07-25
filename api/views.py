from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from api.models import menu_items

class DishesView(APIView):
    def get(self,request,*args,**kwargs):
        all_item=menu_items
        if "category" in request.query_params:
            category=request.query_params.get("category")
            all_item=[item for item in menu_items if item["category"]==category]
        if "limit" in request.query_params:
            count=int(request.query_params.get("limit"))
            return Response(data=all_item[0:count])
        if "price_lt" in request.query_params:
            cost=int(request.query_params.get("price_lt"))
            all_item=[item for item in all_item if item.get("price")<=cost]
        return Response(data=all_item)

    def post(self,request,*args,**kwargs):
        item=request.data
        menu_items.append(item)
        return Response(data=item)

class DishDetailView(APIView):
    def get(self,request,*args,**kwargs):
        code=kwargs.get("dcode")
        item=[item for item in menu_items if item["code"]==code].pop()
        return Response(data=item)
    def put(self,request,*args,**kwargs):
        code=kwargs.get("dcode")
        item = [item for item in menu_items if item["code"] == code].pop()
        data=request.data
        item.update(data)
        return Response(data=data)
    def delete(self,request,*args,**kwargs):
        code=kwargs.get("dcode")
        item = [item for item in menu_items if item["code"] == code].pop()
        menu_items.remove(item)
        return Response(data=item)