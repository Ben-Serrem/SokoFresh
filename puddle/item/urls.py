# Note the creation of a new urls.py file in the item app to bring about order.

from django.urls import path

from . import views

app_name = 'item'

urlpatterns = [
    path('new/', views.new, name='new'),
    path('<int:pk>/', views.detail, name = 'detail')
]