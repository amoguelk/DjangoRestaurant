from django.urls import path, include
from restaurant.views import *

urlpatterns = [
    path("", HomePageView.as_view(), name="home"),
    path("api/", include("rest_framework.urls", namespace="rest_framework")),
    path("server/", ServerList.as_view()),
    path("server/<int:pk>/", ServerDetail.as_view()),
    path("table/", TableList.as_view()),
    path("table/<int:pk>/", TableDetail.as_view()),
    path("customer/", CustomerList.as_view()),
    path("customer/<int:pk>/", CustomerDetail.as_view()),
    path("order/", OrderList.as_view()),
    path("order/<int:pk>/", OrderDetail.as_view()),
    path("item/", ItemList.as_view()),
    path("item/<int:pk>/", ItemDetail.as_view()),
]
