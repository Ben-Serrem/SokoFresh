from django.contrib.auth import views as auth_views
from django.urls import path

from . import views
from .forms import LoginForm

# Several changes have been made that also affect the main urls.py module.
# We brought the contacts code snippet from main urls, so it wasn't required there anymore.
# Also, the main path was changed to path('', include('core.urls'))

app_name = 'core'

urlpatterns = [
    path('', views.index, name='index'),
    path('contacts/', views.contacts, name='contacts'),
    path('signup/', views.signup, name='signup'),
    path('/login/', auth_views.LoginView.as_view(template_name='core/login.html',authentication_form=LoginForm), name='login'),
]