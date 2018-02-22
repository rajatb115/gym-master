from django.conf.urls import url
from entrepreneurship import views

urlpatterns = [
    url(r'^$', views.entrepreneurship,name ='entrepreneurship'),
    url(r'^blog/(?P<slug>[\w-]+)/$', views.entrepreneurship_post, name='view_blog_post'),
    url(r'^blog/category/(?P<slug>[\w-]+)/$', views.entrepreneurship_category, name='view_blog_category')
]

