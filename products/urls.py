from django.conf.urls import url
from products import views

urlpatterns = [
    url(r'^$', views.product,name='product'),
    url(r'^product/(?P<slug>[\w-]+)/$', views.view_product, name='view_product'),
    url(r'^product/category/(?P<slug>[\w-]+)/$', views.product_category, name='view_product_category')
]
