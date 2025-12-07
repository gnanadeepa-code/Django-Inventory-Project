from django.urls import path
from .views import *

urlpatterns = [
   path('', loginPage, name='login'),
   path('logout/', logoutUser, name='logout'),
   path('signup/', signupPage, name='signup'),
]