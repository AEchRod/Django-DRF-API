from rest_framework import serializers
from .models import MenuItem, OrderItem, Order, Cart, Category
from django.contrib.auth.models import User


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'slug', 'title']
class MenuItemSerializer(serializers.ModelSerializer):
    category = CategorySerializer()  # Use CategorySerializer for the nested representation

    class Meta:
        model = MenuItem
        fields = ['title', 'price', 'featured', 'category']

class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = ['user', 'menu_item', 'quantity', 'unit_price', 'price']

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['user', 'delivery_crew', 'status', 'total', 'date']

class OrderItemSerializer(serializers.ModelSerializer):

    #this is a nested relationship
    menu_item = MenuItemSerializer(many=True, read_only=True)

    class Meta:
        model = OrderItem
        fields = ['order', 'menu_item', 'quantity', 'unit_price', 'price']

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'groups', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    #Needed to handle special cases during object creation, i.e. password hashing or additional validation.
    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user



