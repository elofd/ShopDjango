from django.views.generic import DetailView
from django.views.generic.edit import CreateView, UpdateView
from django.contrib.auth.views import LogoutView, LoginView
from django.urls import reverse_lazy
from django.contrib.auth import login

from .models import CustomUser
from .forms import CustomUserCreationForm, CustomUserChangeForm


class CustomUserCreateView(CreateView):
    model = CustomUser
    form_class = CustomUserCreationForm
    template_name = 'users/user_form.html'
    success_url = reverse_lazy('shop:product_list')

    def form_valid(self, form):
        response = super().form_valid(form)
        login(self.request, self.object)
        return response


class CustomUserUpdateView(UpdateView):
    model = CustomUser
    form_class = CustomUserChangeForm
    template_name = 'users/user_form.html'
    success_url = 'shop:product_list'


class CustomUserDetailView(DetailView):
    model = CustomUser
    template_name = 'users/user_detail.html'
    context_object_name = 'user'


class CustomLogoutView(LogoutView):
    next_page = reverse_lazy('shop:product_list')


class CustomLoginView(LoginView):
    template_name = 'users/login.html'
    next_page = reverse_lazy('shop:product_list')

