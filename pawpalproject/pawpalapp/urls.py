from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from .views import *

app_name = 'pawpalapp'

urlpatterns = [
    path('register/', register_user, name='register'),
    # path('', login, name='login'),
    path('accounts/', include('django.contrib.auth.urls'), name='login'),
    # path('', , name='login'),

]