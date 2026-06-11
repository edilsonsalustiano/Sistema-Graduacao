from django.urls import path
from modalidades.views import ListModalidadeView, CreateModalidadeView, UpdateModalidadeView, DeleteModalidadeView


urlpatterns = [

    path('', ListModalidadeView.as_view(), name='lista_modalidades'),
    path('novo/', CreateModalidadeView.as_view(), name='nova_modalidade'),
    path('editar/<int:pk>/', UpdateModalidadeView.as_view(), name='editar_modalidade'),
    path('deletar/<int:pk>/', DeleteModalidadeView.as_view(), name='deletar_modalidade'),

]
