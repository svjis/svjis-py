from . import utils
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout



def main_view(request):
    ctx = {
        'aside_menu_name': 'Články',
        'aside_menu_items': [
            {'description': 'Všechny články', 'link': '/', 'active': True},
            {'description': 'Dokumenty', 'link': '/', 'active': False},
            {'description': 'Smlouvy', 'link': '/', 'active': False},
        ],
    }
    ctx['tray_menu_items'] = utils.get_tray_menu(main_view)
    return render(request, "main.html", ctx)


def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
    return redirect(main_view)


def user_logout(request):
    logout(request)
    return redirect(main_view)


def redaction_view(request):
    ctx = {
        'aside_menu_name': 'Redakce',
        'aside_menu_items': [
            {'description': 'Články', 'link': '/', 'active': True},
        ],
    }
    ctx['tray_menu_items'] = utils.get_tray_menu(redaction_view)
    return render(request, "redaction.html", ctx)
