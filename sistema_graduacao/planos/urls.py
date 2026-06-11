from django.urls import path
from planos.views import ListPlanosView, CreatPlanosView, UpdatePlanosView, DeletePlanosView


urlpatterns = [

    path('', ListPlanosView.as_view(), name='lista_planos'),
    path('novo/', CreatPlanosView.as_view(), name='novo_plano'),
    path('editar/<int:pk>/', UpdatePlanosView.as_view(), name='editar_plano'),
    path('deletar/<int:pk>/', DeletePlanosView.as_view(), name='deletar_plano'),

]
