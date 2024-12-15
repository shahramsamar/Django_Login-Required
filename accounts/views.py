from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin,PermissionRequiredMixin
from django.views.generic import TemplateView



class WelcomeView(PermissionRequiredMixin, LoginRequiredMixin, TemplateView):
    """
    Displays the welcome page after login.
    """
    #for implementation permissions
    permission_required ='accounts.view_login'
    # login_url = '/accounts/login/'  # Corrected login URL
    template_name = 'registration/welcome.html'