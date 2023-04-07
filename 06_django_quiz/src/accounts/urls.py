from django.urls import path
from django.views.generic import TemplateView

from .views import UserLoginView
from .views import UserLogoutView
from .views import UserProfileUpdateView
from .views import UserRegisterView
from .views import user_activate
from .views import user_profile_view

app_name = 'accounts'

urlpatterns = [
    path('register/activate/<str:sign>/', user_activate, name='register_activate'),
    path('register/done/',
         TemplateView.as_view(template_name='accounts/user_register_done.html'), name='register_done'),
    path('register/', UserRegisterView.as_view(), name='register'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('logout/', UserLogoutView.as_view(), name='logout'),
    path('profile/', user_profile_view, name='profile'),
    path('profile/update/', UserProfileUpdateView.as_view(), name='profile_update'),
]
