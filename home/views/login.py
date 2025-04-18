from django.shortcuts import render
from django.views import View
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login
from home.forms import LoginForm


class LoginView(View):
    def get(self, request):
        data = {'form': LoginForm()}
        return render(request, 'home/login.html', data)

    def post(self, request):
        form = LoginForm(data=request.POST)

        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')

            user = authenticate(username=username, password=password)

            if username and password and user:
                login(request, user)
                return HttpResponseRedirect(reverse('index'))

        data = {
            'form': form,
            'error': 'Acesso negado!'
        }

        return render(request, 'home/login.html', data)
