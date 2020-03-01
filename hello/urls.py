
from django.urls import path
from django.conf.urls import include

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('db',views.db,name='db')
    #path('admin/', admin.site.urls),
    #path('api/list', views.get_rest_list, name='get_rest_list'),
]
