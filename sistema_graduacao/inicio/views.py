from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView, ListView
from django.utils import timezone
from modalidades.models import Modalidade
from competicao.models import Competicoes
from planos.models import Plano
from alunos.models import Aluno


class InicioView(LoginRequiredMixin, TemplateView):
    template_name = 'inicio/inicio.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['total_alunos'] = Aluno.objects.count()
        context['total_modalidades'] = Modalidade.objects.count()
        context['total_planos'] = Plano.objects.count()
        context['proximas_competicoes'] = Competicoes.objects.filter(
            data__gte=timezone.localdate()
        ).order_by('data')[:3]
        return context


class ModalidadeListView(ListView):
    model = Modalidade
    template_name = 'modalidades/list.html'
    context_object_name = 'modalidades'


class PlanoListView(ListView):
    model = Plano
    template_name = 'planos/list.html'
    context_object_name = 'planos'
