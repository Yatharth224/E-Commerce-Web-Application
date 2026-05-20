from django.urls import path
from. import views


# URLConf


urlpatterns = [
   # Product URLs
    path('products/', views.product_list, name='product-list'),
    path('products/<int:id>/', views.product_detail, name='product-detail'),

     # Collection URLs
    path('collections/', views.collection_list, name='collection-list'),
    path('collections/<int:id>/', views.collection_detail, name='collection-detail'),

]