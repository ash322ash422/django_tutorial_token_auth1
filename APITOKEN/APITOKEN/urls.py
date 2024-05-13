#from django.contrib import admin
from django.urls import path
from core import views
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    #path('admin/', admin.site.urls),
    path('hello/', views.HelloView.as_view(), name='hello'),
    
    #To get the token for user, send a POST request with username and password. See test_core.py
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),
]
