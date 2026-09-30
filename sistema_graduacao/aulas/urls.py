from django.urls import path
from aulas.views import ListaAulasView, CreateAulasView, UpdateAulasView, DetailAulaView, AdicionarAlunoAulaView, RemoverAlunoAulaView, DeleteAulasView

urlpatterns = [

    path('', ListaAulasView.as_view(), name='lista_aula'),
    path('nova/', CreateAulasView.as_view(), name='nova_aula'),
    path('editar/<int:pk>/', UpdateAulasView.as_view(), name='editar_aula'),
    path('deletar/<int:pk>/', DeleteAulasView.as_view(), name='deletar_aula'),
    path('<int:pk>/', DetailAulaView.as_view(), name='detalhe_aula'),
    path('<int:pk>/adicionar-aluno/', AdicionarAlunoAulaView.as_view(), name='adicionar_aluno_aula'),
    path('<int:pk>/remover-aluno/<int:aluno_pk>/', RemoverAlunoAulaView.as_view(), name='remover_aluno_aula'),

]