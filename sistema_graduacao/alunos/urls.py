from django.urls import path
from alunos.views import ListaAlunosView, CreateAlunoView, UpdateAlunoView, DeleteAlunoView


urlpatterns = [
    path('', ListaAlunosView.as_view(), name='lista_alunos'),
    path('novo/', CreateAlunoView.as_view(), name='novo_aluno'),
    path('editar/<int:pk>/', UpdateAlunoView.as_view(), name='editar_aluno'),
    path('deletar/<int:pk>/', DeleteAlunoView.as_view(), name='deletar_aluno'),

]
