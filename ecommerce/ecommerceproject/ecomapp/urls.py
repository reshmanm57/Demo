from django.urls import path
from . import views
app_name='ecomapp'

urlpatterns = [
    #path('', views.index, name='index')
    path('', views.allproductcat,name='allproductcat'),
    path('<slug:c_slug>/', views.allproductcat, name='products_by_category'),
    path('<slug:c_slug>/<slug:product_slug>/', views.proddetail, name='prod_cat_detail')
]