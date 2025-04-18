from django.urls import path
from home.views.index import IndexView
from home.views.signup import SignUpView
from home.views.login import LoginView
from home.views.logout import LogoutView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('signup/', SignUpView.as_view(), name='signup'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/',LogoutView.as_view(), name='logout'),
]
