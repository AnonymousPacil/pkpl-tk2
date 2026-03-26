from django.urls import path
from main.views import show_anggota, site_settings, login_view, logout_view

app_name = 'main'

urlpatterns = [
    path('', show_anggota, name='show_anggota'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('settings/', site_settings, name='site_settings'),
]
