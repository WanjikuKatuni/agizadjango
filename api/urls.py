from django.urls import path
from . import views


urlpatterns = [
    
    path("customers/", views.CustomerListCreateAPIView.as_view(), name="customer-list"),

    path("customers/details/<int:pk>/", views.CustomerDetailAPIView.as_view(), name="customer-detail"),

    path("customers/details/<int:customer_id>/orders/", views.OrderListCreateAPIView.as_view(), name="order-list"),

    path("orders/details/<int:pk>/", views.OrderDetailAPIView.as_view(), name="order-detail"),

    # path("customer/details/<int:customer_pk>/orders/details/<int:pk>/", views.OrderDetailAPIView.as_view(), name="order-detail")

]