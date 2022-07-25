from rest_framework import serializers

class DishSerializer(serializers.Serializer):
    name=serializers.CharField()
    category=serializers.CharField()
    price=serializers.IntegerField()