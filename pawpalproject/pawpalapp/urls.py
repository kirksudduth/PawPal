from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from .views import *

app_name = 'pawpalapp'

urlpatterns = [
    path('register/', register, name='register'),
    path('accounts/', include('django.contrib.auth.urls'), name='login'),
    path('logout/', logout_user, name='logout'),
    path('pawpals/add', create_pawpal, name='add_pawpal'),
    path('', pawpal_list, name='home'),
    path('pawpals/find', find_pawpal, name='find_pawpal'),
    path('pawpals/<int:pawpal_id>', pawpal_details, name='pawpal_details'),
    path('pawpals/<int:pawpal_id>/add_message', add_message, name='add_message'),
    path('pawpals/<int:pawpal_id>/message_board', message_list, name='message_list'),
    path('pawpals/<int:pawpal_id>/add_activity_type', add_activity_type, name='add_activity_type'),
    path('profile/', profile, name='profile'),
    path('profile/edit', profile_edit, name='profile_edit'),
    path('profile/dedpal', delete_pawpal, name='delete_pawpal'),
    path('activity_types/<int:activity_type_id>', activity_type_details, name='activity_type_details'),
    path('activity_types/<int:activity_type_id>/add_activity', create_activity, name='add_activity'),
] 

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)