from django.urls import path, include
from restaurant import views

urlpatterns = [
    path("", views.index, name="index"),
    path("api/", include("rest_framework.urls", namespace="rest_framework")),
    path("server/", views.ServerList.as_view()),
    path("server/<int:pk>/", views.ServerDetail.as_view()),
    path("table/", views.TableList.as_view()),
    path("table/<int:pk>/", views.TableDetail.as_view()),
    path("customer/", views.CustomerList.as_view()),
    path("customer/<int:pk>/", views.CustomerDetail.as_view()),
    path("order/", views.OrderList.as_view()),
    path("order/<int:pk>/", views.OrderDetail.as_view()),
    path("item/", views.ItemList.as_view()),
    path("item/<int:pk>/", views.ItemDetail.as_view()),
]
