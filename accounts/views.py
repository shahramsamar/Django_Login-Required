from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin,PermissionRequiredMixin
from django.views.generic import TemplateView
from django.urls import reverse, reverse_lazy
from django.views.generic.edit import CreateView
from .forms import CustomUserCreationForm
from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType
from django.contrib import messages
from django.contrib.auth.views import LoginView as BaseLoginView

class CustomLoginView(BaseLoginView):
    template_name = 'registration/login.html'
    redirect_authenticated_user = True

   
    def form_valid(self, form):
        """
        Called when valid form data has been POSTed.
        It should return an HttpResponse.
        """
        # Display a success message to the user upon successful login
        messages.success(self.request, "You have successfully logged in.")
        # Call the parent class's form_valid method to handle the login process
        return super().form_valid(form)

    def form_invalid(self, form):
        """
        Called when invalid form data has been POSTed.
        It should return an HttpResponse.
        """
        # Display an error message to the user when login credentials are invalid
        messages.error(self.request, "Invalid username or password.")
        # Call the parent class's form_invalid method to handle the invalid form submission
        return super().form_invalid(form)
    def get_success_url(self):
        """
        Determines the URL to redirect to after a successful login.
        
        Returns:
            str: The URL to redirect to after successful login.
        """
        # Use the 'reverse' function to get the URL for the 'welcome' view
        return reverse('welcome')

    



class RegisterView(CreateView):
    form_class = CustomUserCreationForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('welcome')

    def form_valid(self, form):
        # Call the parent class's form_valid method and store the response
        response = super().form_valid(form)

        # Save the form and get the newly created user
        user = form.save()

        # Get the 'view_login' permission
        permission = Permission.objects.get(codename='view_login')

        # Add the 'view_login' permission to the new user
        user.user_permissions.add(permission)

        # Display a success message to the user
        messages.success(self.request, 'Your account has been created! You can now log in.')

        # Return the response from the parent class's form_valid method
        return response


    def form_invalid(self, form):
        # Display an error message to the user when registration fails
        messages.error(self.request, 'There was an error with your registration. Please try again.')
        # Call the parent class's form_invalid method to handle the invalid form submission
        return super().form_invalid(form)

    

class WelcomeView(LoginRequiredMixin, TemplateView):
    template_name = 'registration/welcome.html'  # Ensure you have a welcome.html template
    permission_required = 'accounts.view_login'
    login_url = '/login/'  # Ensure this matches your login path


