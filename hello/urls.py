
from django.urls import path
from django.conf.urls import include

from . import views

urlpatterns = [
    #path('party/', views.index, name='/'),
    path('', views.index, name='index'),
    #path('signup/',views.db,name='register')
    path('new/',views.db,name='party_new')
    #path('edit/',views.db,name='party_new')

    path('admin/', admin.site.urls),
]
