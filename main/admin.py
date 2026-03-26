from django.contrib import admin
from .models import Biodata, SiteSetting


@admin.register(Biodata)
class BiodataAdmin(admin.ModelAdmin):
    list_display = ("nama", "NPM", "email", "jenis_kelamin")


@admin.register(SiteSetting)
class SiteSettingAdmin(admin.ModelAdmin):
    list_display = ("background_color", "text_color", "font_family")
