from django.urls import path
from . import views


app_name = 'shop'


urlpatterns = [
    path('', views.ProductListView.as_view(), name='product_list'),
    path('product/<int:pk>/', views.ProductDetailView.as_view(), name='product_detail'),
    path('orders/', views.OrderListView.as_view(), name='order_list'),
    path('add_order/', views.OrderCreateView.as_view(), name='order_create'),
    path('order/<int:pk>/', views.OrderDetailView.as_view(), name='order_detail'),
    path('order/<int:pk>/edit/', views.OrderUpdateView.as_view(), name='order_update'),
    path('order/<int:pk>/delete/', views.OrderDeleteView.as_view(), name='order_delete'),
]
