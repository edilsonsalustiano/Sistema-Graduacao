import logging

from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect

logger = logging.getLogger(__name__)


def login_view(request):

    if request.method == 'POST':
        logger.debug("Tentativa de autenticação recebida")

        username = request.POST.get('username')
        password = request.POST.get('password')

        try:
            user = authenticate(
                request,
                username=username,
                password=password
            )

            if user is not None:
                login(request, user)

                logger.info("Login realizado com sucesso")

                return redirect('inicio')

            logger.warning("Tentativa de login recusada")

            messages.error(
                request,
                'Usuário ou senha incorretos.'
            )

        except Exception:
            logger.exception(
                "Erro inesperado durante o processamento do login"
            )
            raise

    return render(request, 'login/login.html')