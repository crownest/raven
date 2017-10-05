# Django
from django.conf import settings
from django.contrib import messages
from django.views.static import serve
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.views.generic import View, TemplateView, RedirectView


# Local Django
from raven.forms import LoginForm, RegisterForm
from raven.variables import LOGIN_FORM_PREFIX, REGISTER_FORM_PREFIX
from departments.models import Department
from users.models import User
from users.variables import USER_TYPES, TEACHER


class DocumentationView(View):

    def get(self, request, path='index.html', **kwargs):
        return serve(
            request, path, document_root=settings.DOCUMENTATION_ROOT, **kwargs
        )


class LandingView(TemplateView):
    template_name = 'landing.html'

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated():
            return redirect('index')

        return super(LandingView, self).dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(LandingView, self).get_context_data(**kwargs)

        context.update({
            'title': 'Welcome',
            'login_form': LoginForm(prefix=LOGIN_FORM_PREFIX)
        })

        return context

    def post(self, request, *args, **kwargs):
        context = self.get_context_data()

        if LOGIN_FORM_PREFIX in request.POST:
            login_form = LoginForm(request.POST, prefix=LOGIN_FORM_PREFIX)
            context.update({'login_form': login_form})

            if login_form.is_valid() and login_form.user:
                auth_login(request, login_form.user)

                return HttpResponseRedirect(reverse('index'))

        return super(LandingView, self).render_to_response(context)


class LogoutView(RedirectView):
    permanent = False
    query_string = True
    pattern_name = 'landing'

    def get_redirect_url(self, *args, **kwargs):
        if self.request.user.is_authenticated():
            auth_logout(self.request)

        return super(LogoutView, self).get_redirect_url(*args, **kwargs)


class RegisterView(TemplateView):
    template_name = 'register.html'

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated():
            return redirect('index')

        return super(RegisterView, self).dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(RegisterView, self).get_context_data(**kwargs)

        context.update({
            'title': 'Register',
            'register_form': RegisterForm(prefix=REGISTER_FORM_PREFIX)
        })

        return context

    def post(self, request, *args, **kwargs):
        context = self.get_context_data()

        if REGISTER_FORM_PREFIX in request.POST:
            registration_request = None
            register_form = RegisterForm(request.POST, prefix=REGISTER_FORM_PREFIX)

            if register_form.is_valid():
                registration_request = register_form.save()

            if registration_request:
                messages.success(
                    request, 'Your registration request has been received.'
                )
            else:
                messages.error(
                    request, 'Your registration request was not received. Try again!'
                )

            context.update({'register_form': register_form})

        return super(RegisterView, self).render_to_response(context)


class IndexView(TemplateView):
    template_name = 'index.html'

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated():
            return redirect('landing')

        return super(IndexView, self).dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        departments = Department.objects.filter(
            name__in=self.request.user.departments.all().values("name"),
            college__name=self.request.user.college
        )
        teachers = User.objects.filter(
            user_type=TEACHER, departments=self.request.user.departments.all()
        ).order_by('first_name')

        context.update({
            'title': 'Index',
            'departments': departments,
            'teachers': teachers
        })

        return context


class RegistrationRequestView(TemplateView):
    template_name = 'registration-request.html'

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated():
            return redirect('landing')

        return super(RegisterView, self).dispatch(request, *args, **kwargs)
