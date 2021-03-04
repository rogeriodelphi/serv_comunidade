from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# Create your views here.


def user_login(request):
    template_name = 'account/login.html'
    context = {}
    if request.method == 'POST':
        usuario = request.POST.get('usuario')
        senha = request.POST.get('senha')
        user = authenticate(request, username=usuario, password=senha)
        if user is not None:
            login(request, user)
            return redirect('account:area_logada')
        else:
            messages.error(request, 'Usuário ou senha inválido')
    return render(request, template_name, context)


@login_required
def area_logada(request):
    template_name = 'account/area_logada.html'
    context = {}
    return render(request, template_name, context)


@login_required
def user_logout(request):
    logout(request)
    return redirect('account:user_login')