from django.urls import path
from. import views


# URLConf


urlpatterns = [
   
    path('products/', views.product_list, name='product-list'),

    path('products/<int:id>/', views.product_detail, name='product-detail'),

    path('collections/', views.collection_list, name='collection-list'),

    path('collections/<int:id>/', views.collection_detail, name='collection-detail'),

    path('carts/create/', views.create_cart, name='create-cart'),
    
    path('orders/create/<int:customer_id>/', views.create_order, name='create-order'),

    path('carts/<int:cart_id>/add/<int:product_id>/', views.add_to_cart, name='add-to-cart'),

    path('customers/', views.customer_list, name='customer-list'),


]