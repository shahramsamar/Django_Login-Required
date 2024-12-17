

from django.urls import path
from .views import WelcomeView, RegisterView, CustomLoginView

urlpatterns = [
    path('', WelcomeView.as_view(), name='welcome'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('register/', RegisterView.as_view(), name='register'),
]
