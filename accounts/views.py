from django.contrib.auth.forms import UserChangeForm
from django.urls import reverse_lazy
from django.views.generic import CreateView, TemplateView
from .forms import UserAddForm
from django.contrib.auth.views import PasswordChangeView, PasswordChangeDoneView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages


class SignUpView(CreateView): 
    form_class = UserAddForm
    success_url = reverse_lazy('login') 
    template_name = 'registration/signup.html'

class UserProfileView(LoginRequiredMixin, TemplateView): 
     template_name = 'userprofile.html'