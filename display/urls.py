from django.urls import path
from . import views

app_name='display'
urlpatterns = [
    #path('',views.home,name='home'),
    path('reg',views.reg, name="reg"),
    path('reg1',views.reg1, name="reg1"),
    # path('reg2',views.reg2, name="reg2"),
] 
