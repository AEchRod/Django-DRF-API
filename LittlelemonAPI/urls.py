from django.urls import path
from . import views

urlpatterns = [
    # Menu Items Endpoints
    path('menu-items/', views.MenuItemsView.as_view(), name='list_create_menu_items'),
    path('menu-items/<int:pk>/', views.SingleMenuItemView.as_view(), name='single_menu_item'),

    # Order Management Endpoints
    path('orders/', views.OrderView.as_view(), name='list_create_orders'),
    path('orders/<int:pk>/', views.SingleOrderView.as_view(), name='list_items_in_order'),
    path('orders/delivery-crew/', views.DeliveryCrewOrderView.as_view(), name='delivery_crew_orders'),
    path('orders/update/<int:pk>/', views.DeliveryCrewUpdateOrderView.as_view(), name='update_order_status'),

    # Cart Management Endpoints
    path('cart/menu-items/', views.CartItemsView.as_view(), name='list_create_cart_items'),

    #User Management Endpoints
    path('groups/manager/users/', views.ManagerUsersView.as_view(), name='manager_users'),
    path('groups/delivery-crew/users/', views.DeliveryCrewUsersView.as_view(), name='delivery_crew_users'),
]

"""
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import MenuItemList, MenuItemDetail, ManagerUserList, ManagerUserDetail, \
    DeliveryCrewUserList, DeliveryCrewUserDetail, CartItemList, CartItemDetail, OrderList, OrderDetail, \
    CustomUserViewSet

# Create a router and register our viewset with it.
router = DefaultRouter()
router.register(r'users', CustomUserViewSet, basename='user')

# The API URLs are now determined automatically by the router.
urlpatterns = [

    # User Registration and Token Generation Endpoints
    path('token/login/', include('djoser.urls.authtoken')),

    # Menu Items Endpoints
    path('menu-items/', MenuItemList.as_view(), name='menu-item-list'),
    path('amenu-items/<int:pk>/', MenuItemDetail.as_view(), name='menu-item-detail'),

    # User Group Management Endpoints
    path('groups/manager/users/', ManagerUserList.as_view(), name='manager-user-list'),
    path('groups/manager/users/<int:pk>/', ManagerUserDetail.as_view(), name='manager-user-detail'),
    path('groups/delivery-crew/users/', DeliveryCrewUserList.as_view(), name='delivery-crew-user-list'),
    path('groups/delivery-crew/users/<int:pk>/', DeliveryCrewUserDetail.as_view(), name='delivery-crew-user-detail'),

    # Cart Management Endpoints
    path('cart/menu-items/', CartItemList.as_view(), name='cart-item-list'),
    path('cart/menu-items/<int:pk>/', CartItemDetail.as_view(), name='cart-item-detail'),

    # Order Management Endpoints
    path('orders/', OrderList.as_view(), name='order-list'),
    path('orders/<int:pk>/', OrderDetail.as_view(), name='order-detail'),
    ] """