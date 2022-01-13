from django.urls import path

from . import views


urlpatterns = [
    path('home/', views.Home.as_view(), name="home"),
    path('product/', views.Products.as_view(), name="product"),
    path('add/', views.AddProduct.as_view(), name="add_product"),
    path('update/', views.UpdateProduct.as_view(), name="update_product"),
    path('merchant/', views.Merchants.as_view(), name="merchant"),
    path('merchant/add/', views.AddMerchant.as_view(), name="add_merchant"),
    path('merchantdetail/<str:code>/', views.MerchantDetail.as_view(), name="merchant_detail"),
]