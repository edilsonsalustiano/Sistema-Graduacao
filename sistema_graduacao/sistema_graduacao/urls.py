from django.contrib import admin
from django.urls import path, include

urlpatterns = [


    path('admin/', admin.site.urls),

    path('', include('login.urls')),

    path('inicio/', include('inicio.urls')),

    path('alunos/', include('alunos.urls')),

    path('modalidades/', include('modalidades.urls')),

    path('planos/', include('planos.urls')),

]
