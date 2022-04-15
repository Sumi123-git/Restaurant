from django.urls import path
from .import views
app_name='restrrapp'

urlpatterns = [
    path('',views.register1,name='register1'),

]
