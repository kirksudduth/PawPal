from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from .views import *

app_name = 'pawpalapp'

urlpatterns = [
    path('register/', register, name='register'),
    path('', activity_type_list, name='home'),
    path('accounts/', include('django.contrib.auth.urls'), name='login'),
    path('logout/', logout_user, name='logout'),
    path('pawpals/add', create_pawpal, name='add_pawpal'),
    path('profile/', profile, name='profile'),
    path('profile/edit', profile_edit, name='profile_edit'),
    path('activity_types/<int:activity_type_id>', activity_type_details, name='activity_type_details'),
    path('activity_types/<int:activity_type_id>/add_activity', create_activity, name='add_activity'),
]