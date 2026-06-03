from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect

def login_view(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        print("Usuário:", username)
        print("Senha:", password)

        user = authenticate(
            request,
            username=username,
            password=password
        )

        print("Resultado:", user)

        if user is not None:
            login(request, user)
            return redirect('inicio')

        messages.error(request, 'Usuário ou senha incorretos.')

    return render(request, 'login/login.html')