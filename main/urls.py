from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('process_color', views.process_color),
    path('show_color', views.show_color),
]
