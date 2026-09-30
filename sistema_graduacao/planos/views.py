from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from .models import Plano


class ListPlanosView(LoginRequiredMixin, ListView):
    model = Plano
    template_name = 'planos/list.html'
    context_object_name = 'planos'


class CreatPlanosView(LoginRequiredMixin, CreateView):
    model = Plano
    template_name = 'planos/form.html'
    fields = '__all__'
    success_url = reverse_lazy('lista_planos')


class UpdatePlanosView(LoginRequiredMixin, UpdateView):
    model = Plano
    template_name = 'planos/form.html'
    fields = '__all__'
    success_url = reverse_lazy('lista_planos')


class DeletePlanosView(LoginRequiredMixin, DeleteView):
    model = Plano
    template_name = 'planos/delete.html'
    success_url = reverse_lazy('lista_planos')
