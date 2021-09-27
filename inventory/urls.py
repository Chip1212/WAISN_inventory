from django.urls import path
from django.conf.urls import include, url
from . import views
from django.contrib.auth import logout, login

app_name = 'inventory'

urlpatterns = [

    path('', views.index, name='index'),
    path('<int:item_id>/', views.detail, name='detail'),
    path('<int:item_id>/manage/', views.manage, name='manage'),
    path('new_item', views.new_item, name='new_item'),
    path('create_item', views.create_item, name='create_item'),
    path('accounts/', include('django.contrib.auth.urls')),
]
