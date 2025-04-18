from django.shortcuts import render, redirect
from django.views import View
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from home.forms import SignupForm

class SignUpView(View):
    def get(self, request):
        data = { 'form': SignupForm() }
        return render(request, 'home/signup.html', data)
    
    
    def post(self, request):
        form = SignupForm(data=request.POST)

        if form.is_valid():
            username = form.cleaned_data.get('username')
            password1 = form.cleaned_data.get('password1')
            password2 = form.cleaned_data.get('password2')
            
            if username and password1 and password2 \
                and password1 == password2:

                user = User.objects.create_user(
                    username = username,
                    password = password1
                )

                if user:
                    return HttpResponseRedirect(reverse('login'))
        
        data = { 
            'form': form,
            'error': 'Usuário ou senha inválidos'
        }     
        return render(request, 'home/signup.html', data)