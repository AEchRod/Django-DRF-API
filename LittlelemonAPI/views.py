from .models import MenuItem, OrderItem, Order, Cart
from rest_framework import generics, status
from .serializers import MenuItemSerializer, OrderItemSerializer, OrderSerializer, CartSerializer, UserSerializer
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from .permissions import IsManager, IsDeliveryCrew, IsCustomer
from rest_framework.exceptions import PermissionDenied
from rest_framework.response import Response
from django.contrib.auth.models import User


#Manager can create menu items and see list of all menu items
class MenuItemsView(generics.ListCreateAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer

    def get_permissions(self):
        if self.request.method == 'GET':
            return [IsAuthenticated()]  # Customers and Delivery Crew can list menu items
        elif self.request.method in ['POST']:
            if IsManager().has_permission(self.request, self):  # Instantiate IsManager and check permission
                return [IsManager()]  # Only Managers can create, update, or delete menu items
            else:
                raise PermissionDenied()  # Deny access and return 403 - Unauthorized

        return [IsAuthenticated()]

"""class MenuItemsView(generics.RetrieveUpdateDestroyAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer

    def get_permissions(self):
        if self.request.method == 'GET':
            return [IsManager(), IsCustomer(), IsDeliveryCrew()]  # Customers and Delivery Crew can list menu items
        elif self.request.method in ['POST', 'PUT', 'PATCH', 'DELETE']:
            if IsManager():
                return [IsManager()]  # Only Managers can create, update, or delete menu items
            else:
                raise PermissionDenied()  # Deny access and return 403 - Unauthorized

        return [IsAuthenticated()]"""

class SingleMenuItemView(generics.RetrieveUpdateDestroyAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer

    def get_permissions(self):
        if self.request.method == 'GET':
            return [IsAuthenticated()]  # Customers and Delivery Crew can list menu items
        elif self.request.method in ['PUT', 'PATCH', 'DELETE']:
            if IsManager():
                return [IsManager()]  # Only Managers can create, update, or delete menu items
            else:
                raise PermissionDenied()  # Deny access and return 403 - Unauthorized
        return [IsAuthenticated()]


class OrderView(generics.ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    def get_permissions(self):
        if self.request.method == 'GET':
            return [IsCustomer()]  # Only Customers can retrieve their own orders
        elif self.request.method == 'POST':
            return [IsCustomer()]  # Customers can create their own orders
        return [IsAuthenticated()]


#RetrieveUpdateDestroy used for read-write-delete endpoints to represent a single model instance.
class SingleOrderView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    def get_permissions(self):
        if self.request.method == 'DELETE':
            return [IsManager()]
        elif self.request.method == ['GET', 'PATCH', 'PUT']:
            return [IsDeliveryCrew(), IsCustomer()]
        return [IsAuthenticated()]


class DeliveryCrewOrderView(generics.ListAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    def get_permissions(self):
        if self.request.method == 'GET':
            return [IsDeliveryCrew()]  # Only Delivery Crew can access their assigned orders
        return [IsAuthenticated()]


class DeliveryCrewUpdateOrderView(generics.UpdateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    def get_permissions(self):
        if self.request.method == 'PATCH':
            # Check if the order belongs to the delivery crew
            if self.get_object().delivery_crew == self.request.user:
                return [IsDeliveryCrew()]
            else:
                raise PermissionDenied()
        return [IsAuthenticated()]


class CartItemsView(generics.ListCreateAPIView):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer

    def get_permissions(self):
        if self.request.method == 'GET':
            return [IsCustomer()]  # Only Customers can view their own cart items
        elif self.request.method == 'POST':
            return [IsCustomer()]  # Customers can add items to their cart
        elif self.request.method == 'DELETE':
            return [IsCustomer()]  # Customers can delete their own cart items
        return [IsAuthenticated()]  # For other methods (PUT, PATCH, DELETE), require authentication"""


class ManagerUsersView(generics.ListCreateAPIView):
    queryset = User.objects.filter(groups__name='Manager')
    serializer_class = UserSerializer

    def get_permissions(self):
        if self.request.method == ['GET', 'POST', 'DELETE']:
            return [IsManager()]
        return [IsAuthenticated()]

    def delete(self, request, *args, **kwargs):
        # Implement the logic to delete a user by username
        username = request.data.get('username')
        try:
            user = User.objects.get(username=username, groups__name='Manager')
            user.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except User.DoesNotExist:
            return Response({'detail': 'User not found.'}, status=status.HTTP_404_NOT_FOUND)


class DeliveryCrewUsersView(generics.ListCreateAPIView):
    queryset = User.objects.filter(groups__name='Delivery_crew')
    serializer_class = UserSerializer

    def get_permissions(self):
        if self.request.method == ['GET', 'POST', 'DELETE']:
            return [IsManager()]
        return [IsAuthenticated()]

    def delete(self, request, *args, **kwargs):
        # Implement the logic to delete a user by username
        username = request.data.get('username')
        try:
            user = User.objects.get(username=username, groups__name='Delivery_crew')
            user.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except User.DoesNotExist:
            return Response({'detail': 'User not found.'}, status=status.HTTP_404_NOT_FOUND)

"""
from rest_framework import generics, permissions
from .models import MenuItem, User, Cart, Order
from .serializers import MenuItemSerializer, UserSerializer, CartSerializer, OrderSerializer
from .permissions import IsManager, IsDeliveryCrew, IsCustomer, IsOwner
from djoser.views import UserViewSet
from rest_framework.permissions import AllowAny

class CustomUserViewSet(UserViewSet):
    permission_classes = [AllowAny]  # No authentication required for registration

class MenuItemList(generics.ListCreateAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer
    permission_classes = [IsCustomer]  # Only customers can access this endpoint for listing menu items

    def get_permissions(self):
        if self.request.method == 'GET':
            return [permissions.AllowAny()]  # Allow anyone to view menu items
        elif self.request.method in ['POST', 'PUT', 'PATCH', 'DELETE']:
            return [IsCustomer()]  # Only customers can perform write operations on menu items

class MenuItemDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer
    permission_classes = [IsManager]  # Only managers can update/delete menu items

class ManagerUserList(generics.ListCreateAPIView):
    queryset = User.objects.filter(groups__name='Manager')
    serializer_class = UserSerializer
    permission_classes = [IsManager]

class ManagerUserDetail(generics.RetrieveDestroyAPIView):
    queryset = User.objects.filter(groups__name='Manager')
    serializer_class = UserSerializer
    permission_classes = [IsManager]

class DeliveryCrewUserList(generics.ListCreateAPIView):
    queryset = User.objects.filter(groups__name='Delivery Crew')
    serializer_class = UserSerializer
    permission_classes = [IsManager]

class DeliveryCrewUserDetail(generics.RetrieveDestroyAPIView):
    queryset = User.objects.filter(groups__name='Delivery Crew')
    serializer_class = UserSerializer
    permission_classes = [IsManager]

class CartItemList(generics.ListCreateAPIView):
    serializer_class = CartSerializer
    permission_classes = [IsCustomer]  # Only customers can access their own cart items

    def get_queryset(self):
        if self.request.method == 'GET':
            return Cart.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        # Set customer-specific fields during creation if needed
        serializer.save(user=self.request.user)

class CartItemDetail(generics.DestroyAPIView):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer
    permission_classes = [IsCustomer, IsOwner]  # Only customers can delete their own cart items

class OrderList(generics.ListCreateAPIView):
    serializer_class = OrderSerializer
    permission_classes = [IsCustomer]  # Only customers can create/view their own orders

    def get_queryset(self):
        if self.request.method == 'GET':
            return Order.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        # Set customer-specific fields during creation if needed
        serializer.save(user=self.request.user)

class OrderDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [IsManager]  # Managers can update/delete orders"""
