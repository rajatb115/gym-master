from django.conf.urls import url
from politics import views

urlpatterns = [
    url(r'^$', views.index,name='politics'),
    url(r'^blog/(?P<slug>[\w-]+)/$', views.view_post, name='view_politics_post'),
    url(r'^blog/category/(?P<slug>[\w-]+)/$', views.view_category, name='view_politics_category')
]
