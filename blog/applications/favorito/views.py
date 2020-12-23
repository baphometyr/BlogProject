from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView
from django.views import View
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect
# Models
from .models import Favorites
from applications.entrada.models import Entry


class UserPageListView(LoginRequiredMixin, ListView):
    template_name = "favorito/perfil.html"
    context_object_name = "entradas_user"
    login_url = reverse_lazy("users_app:user-login")

    def get_queryset(self):
        return Favorites.objects.entradas_user(self.request.user)
        #return super(UserPageListView, self).get_queryset()

class AddFavoriteView(LoginRequiredMixin, View):
    login_url = reverse_lazy("users_app:user-login")

    def post(self, request, *args, **kwargs):
        user = self.request.user
        entry = Entry.objects.get(id=self.kwargs['pk'])
        Favorites.objects.create(
            user=user,
            entry=entry
        )

        return HttpResponseRedirect(reverse_lazy('favorite_app:favoritos'))

class DeleteFavoriteView(LoginRequiredMixin, View):
    login_url = reverse_lazy("users_app:user-login")

    def post(self, request, *args, **kwargs):
        user = self.request.user
        entry = Entry.objects.get(id=self.kwargs['pk'])
        Favorites.objects.get(
            user=user,
            entry=entry
        ).delete()

        return HttpResponseRedirect(reverse_lazy('favorite_app:favoritos'))
