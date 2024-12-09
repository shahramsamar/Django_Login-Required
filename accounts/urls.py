from django.urls import path, include
from .views import WelcomeView


urlpatterns = [
    path('', WelcomeView.as_view(), name='welcome'),
    # Other URLs like login, logout, dashboard, etc.
]