from django.urls import path

from . import views

app_name = 'shop'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('detail/<int:item_id>/', views.item_detail, name='detail')
]