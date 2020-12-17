import datetime
#
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy, reverse

from django.views.generic import (
    TemplateView,
    CreateView,
)
# Models
from applications.entrada.models import Entry
from .models import Home
# Forms
from .forms import SuscribersForm

class HomePageView(TemplateView):
    template_name = "home/index.html"

    def get_context_data(self, **kwargs):
        context = super(HomePageView, self).get_context_data(**kwargs)
        context["home"] = Home.objects.latest('created')
        context["portada"] = Entry.objects.entrada_portada()
        context["entradas_home"] = Entry.objects.entrada_home()
        context["entradas_recientes"] = Entry.objects.entradas_recientes()
        # Eviamos formulario de suscribcion
        context["formulario"] = SuscribersForm
        return context
    

class SuscribersCreateView(CreateView):
    form_class = SuscribersForm
    success_url = '.'
