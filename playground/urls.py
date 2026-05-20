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

      # Cart URLs
    path('carts/create/', views.create_cart, name='create-cart'),
    path('carts/<int:cart_id>/add/<int:product_id>/', views.add_to_cart, name='add-to-cart'),

     # Order URLs
    path('orders/create/<int:customer_id>/', views.create_order, name='create-order'),

      # Customer URLs
    path('customers/', views.customer_list, name='customer-list'),

]