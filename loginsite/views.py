from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import redirect
from django.urls import reverse, reverse_lazy
from django.views.generic import TemplateView, FormView, UpdateView
from loginsite.forms import RegisterForm, RegisterForm


User = get_user_model()

class SiteLoginView(LoginView):
    template_name = 'loginsite/login.html'

class SiteLoginViewOk(TemplateView):
    template_name = 'loginsite/login_ok.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['username'] = self.request.GET.get('username')
        return context



class SiteRegister_ok(TemplateView):
    template_name = 'loginsite/register_ok.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['username'] = self.request.GET.get('username')
        return context

class SiteLogoutView(LogoutView):
    template_name = 'loginsite/logout.html'

class SiteRegister(FormView):
    template_name = 'loginsite/register.html'
    form_class = RegisterForm

    def form_valid(self, form):
        data = form.cleaned_data
        new_user = User.objects.create_user(
            username=data['username'],
            email=data['email'],
            password=data['password2']
        )
        url = f"{reverse('register_ok')}?username={new_user.username}"
        return redirect(url)


class ProfileEditView(LoginRequiredMixin, UpdateView):
    template_name = 'loginsite/profile.html'
    model = User
    fields = ('full_name','address', 'year_birth', 'about')
    success_url = reverse_lazy('profile')

    def get_object(self, queryset=None):
        return self.request.user
