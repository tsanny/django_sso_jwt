from django.urls import path
from .cas.views import LoginView, LogoutView

app_name = 'sso_auth'
urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
]
