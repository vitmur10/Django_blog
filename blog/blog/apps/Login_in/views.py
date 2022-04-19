from django.shortcuts import render
from django.views.generic.edit import FormView
from django.views.generic import TemplateView
#from
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect
from django.views.generic.base import View
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm


class MainView(TemplateView):
    template_name = 'button.html'

    def get(self, request):
        if requests.user.is_autheticated:
            return render(request, self.template_name, {})


class RegisterFormView(FormView):
    form_class = UserCreationForm
    success_url = 'in/login/'

    template_name = 'register.html'

    def form_valid(self, form):
        form.save()
        return super(RegisterFormView, self).form_valid(form)

    def form_invalid(self, form):

        return super(RegisterFormView, self).form_invalid(form)


