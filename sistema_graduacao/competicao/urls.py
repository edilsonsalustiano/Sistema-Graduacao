from django.urls import path
from competicao.views import ListaCompeticoesView, CreateCompeticoesView, UpdateCompeticoesView, DetailCompeticoesView, DeleteCompeticoesView, AdicionarAlunoCompeticaoView, RemoverInscricaoView


urlpatterns = [

    path('', ListaCompeticoesView.as_view(), name='lista_competicoes'),
    path('novo/', CreateCompeticoesView.as_view(), name='nova_competicao'),
    path('editar/<int:pk>/', UpdateCompeticoesView.as_view(), name='editar_competicao'),
    path('detalhes/<int:pk>/', DetailCompeticoesView.as_view(), name='detalhes_competicao'),
    path('deletar/<int:pk>/', DeleteCompeticoesView.as_view(), name='deletar_competicao'),
    path('adicionar/<int:pk>/', AdicionarAlunoCompeticaoView.as_view(), name="adicionar"),
    path('remover/<int:pk>/', RemoverInscricaoView.as_view(), name='remover_inscricao'),

]