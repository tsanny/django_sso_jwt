from django.urls import path
from .cas.views import LoginView, LogoutView
from rest_framework.authtoken import views as views_token

app_name = 'sso_auth'
urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('api-auth-token/', views_token.obtain_auth_token, name='api-auth-token'),
]
