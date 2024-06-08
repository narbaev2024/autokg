from rest_framework import serializers
from .models import Category, CarMake, Model, Car

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class CarMakeSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarMake
        fields = '__all__'

class ModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Model
        fields = '__all__'

class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = ['car_name', 'description', 'price', 'year', 'mileage', 'color', 'drive', 'engine', 'volume', 'category', 'car_make', 'car_model']

