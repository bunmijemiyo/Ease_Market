from django.urls import path
from .views import ProfileView

urlpatterns = [
    #path('', MenuView.as_view(), name='menu'),
    path('', ProfileView.as_view(), name='home'),
]