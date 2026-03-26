from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.http import HttpResponseForbidden
from .models import Biodata, SiteSetting


def is_member(user):
    if not user.is_authenticated:
        return False
    return Biodata.objects.filter(email=user.email).exists()


def show_anggota(request):
    anggota = Biodata.objects.all()

    settings = SiteSetting.load()

    context = {
        "anggota": anggota,
        "font": settings.font_family,
        "warna": settings.text_color,
        "bg_color": settings.background_color,
        "is_member": is_member(request.user),
        "current_page": "home",
    }

    return render(request, "main.html", context)


@login_required
def site_settings(request):
    if not is_member(request.user):
        return HttpResponseForbidden(
            "<h1>403 Forbidden</h1>"
            "<p>Only group members can modify site settings.</p>"
            "<p>Your email is not registered in the member list.</p>"
            "<a href='/'>Back to Homepage</a>"
        )

    settings = SiteSetting.load()

    if request.method == "POST":
        settings.background_color = request.POST.get(
            "background_color", settings.background_color
        )
        settings.text_color = request.POST.get("text_color", settings.text_color)
        settings.font_family = request.POST.get("font_family", settings.font_family)
        settings.save()
        return redirect("main:show_anggota")

    context = {
        "settings": settings,
        "is_member": True,
        "current_page": "settings",
    }
    return render(request, "settings.html", context)


def login_view(request):
    return redirect("/accounts/google/login/")


def logout_view(request):
    logout(request)
    return redirect("main:show_anggota")
