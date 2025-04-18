from django.shortcuts import render
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin

class IndexView(View):
        def get(self, request):
                data = { 'user': request.user }
                return render(request, 'home/index.html', data)