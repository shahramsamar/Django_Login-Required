from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView



class WelcomeView(LoginRequiredMixin, TemplateView):
    """
    Displays the welcome page after login.
    """
    # login_url = '/accounts/login/'  # Corrected login URL
    template_name = 'welcome.html'