from django.urls import path
from api import views

urlpatterns = [
    # LINE Bot
    path('callback/', views.callback, name="LINE-Bot-Callback"),
]