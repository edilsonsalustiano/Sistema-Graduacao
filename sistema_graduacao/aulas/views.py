from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views import View
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView, FormView
from aulas.form import AulaForm, HorarioFormSet, AdicionarAlunoForm
from django.shortcuts import redirect, get_object_or_404
from django.urls import reverse_lazy
from aulas.models import Aula


class ListaAulasView(LoginRequiredMixin, ListView):
    model = Aula
    template_name = 'aulas/lista_aulas.html'
    context_object_name = 'aulas'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['total_aulas'] = Aula.objects.count()
        return context


class HorarioFormsetMixin:
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.POST:
            context['formset'] = HorarioFormSet(self.request.POST, instance=self.object)
        else:
            context['formset'] = HorarioFormSet(instance=self.object)
        return context

    def form_valid(self, form):
        formset = self.get_context_data()['formset']
        if formset.is_valid():
            self.object = form.save()
            formset.instance = self.object
            formset.save()
            return redirect(self.get_success_url())
        return self.render_to_response(self.get_context_data(form=form))


class CreateAulasView(LoginRequiredMixin, HorarioFormsetMixin, CreateView):
    model = Aula
    form_class = AulaForm
    template_name = 'aulas/form_aulas.html'
    success_url = reverse_lazy('lista_aula')


class UpdateAulasView(LoginRequiredMixin,  HorarioFormsetMixin, UpdateView):
    model = Aula
    form_class = AulaForm
    template_name = 'aulas/form_aulas.html'
    success_url = reverse_lazy('lista_aula')


class DeleteAulasView(LoginRequiredMixin, DeleteView):
    model = Aula
    template_name = 'aulas/delete_aulas.html'
    success_url = reverse_lazy('lista_aula')


class DetailAulaView(LoginRequiredMixin, DetailView):
    model = Aula
    template_name = 'aulas/detalhe_aula.html'
    context_object_name = 'aula'
    queryset = Aula.objects.prefetch_related('horarios', 'alunos')


class AdicionarAlunoAulaView(LoginRequiredMixin, FormView):
    template_name = 'aulas/adicionar_aluno.html'
    form_class = AdicionarAlunoForm

    def get_aula(self):
        return get_object_or_404(Aula, pk=self.kwargs['pk'])

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['aula'] = self.get_aula()
        return kwargs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['aula'] = self.get_aula()
        return context

    def form_valid(self, form):
        self.get_aula().alunos.add(form.cleaned_data['aluno'])
        return redirect('detalhe_aula', pk=self.kwargs['pk'])


class RemoverAlunoAulaView(LoginRequiredMixin, View):
    def post(self, request, pk, aluno_pk):
        aula = get_object_or_404(Aula, pk=pk)
        aula.alunos.remove(aluno_pk)
        return redirect('detalhe_aula', pk=pk)