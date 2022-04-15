from django.urls import path
from .import views
app_name='credentials'
urlpatterns = [
    path('register',views.register,name='register'),
    path('login',views.login,name='login'),
    path('foodbooking', views.booking,name='booking'),
#     path('slug:c_slug/',views.allproductcat,name='allproductcat')
]
