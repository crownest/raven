# Django
from django.views.generic import TemplateView
from django.contrib.auth import login
from django.shortcuts import render, redirect

# Local Django
from raven.forms import LoginForm


class LoginView(TemplateView):
    template_name = 'login.html'

    def post(self, request, *args, **kwargs):
        form = LoginForm(request.POST or None)
        if form.is_valid():
            login(request, form.get_user())
            return redirect('/')
        return render(request, self.template_name, {'form': form})


def IndexView(request):

    return render(request, 'index.html')
