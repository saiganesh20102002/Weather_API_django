from . import views
from django.urls import path,include
from.views import *

urlpatterns = [
    path('',views.home,name="home")

]
