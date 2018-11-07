from django.conf.urls import url
from apps.core.views import index
from django.urls import path
app_name = 'core'

urlpatterns = [
   url(r'^$',index,name='index')
]