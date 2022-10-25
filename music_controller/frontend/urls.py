# from . import views
from . import views
from django.urls import path


# we have to add the new paths here too for django to know what to d
urlpatterns = [
    path('', views.index),
    path('join',views.index)
]   
