from django.urls import path
from main.views import show_anggota

app_name = 'main'

urlpatterns = [
    path('', show_anggota, name='show_anggota'),
]