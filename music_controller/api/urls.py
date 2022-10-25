from django.urls import path
from . import views



#from .views import main why didnt this work ? Ask ribal, 



urlpatterns = [
    path('room',views.RoomView.as_view()),
]