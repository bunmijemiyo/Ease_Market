from django.urls import path, re_path
from .views import (ProfileView, LoginView, logout_view, SignupView, seller_create, SellerListView, seller_detail)

app_name = 'seller'
urlpatterns = [
    #path('', MenuView.as_view(), name='menu'),
    path('', ProfileView.as_view(), name='home'),
    re_path('signup/?', SignupView.as_view(), name='signup'),
    re_path('login/?', LoginView.as_view(), name='login'),
    path('logout/', logout_view, name='logout'),
    re_path('create/?', seller_create, name='create_product'),
    path('list', SellerListView.as_view(), name='seller_list'),
    re_path (r'^(?P<slug>[\w-]+)', seller_detail, name='detail'),
]