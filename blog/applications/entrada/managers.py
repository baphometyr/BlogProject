from django.db import models
from django.db.models import Q

class EntryManager(models.Manager):
    """ Manager del modelo Entry """

    def entrada_portada(self):
        return self.filter(
            public=True,
            portada=True
        ).order_by('-created').first()
    
    def entrada_home(self):
        # devuelve las ultimas 4 entradas en home
        return self.filter(
            public=True,
            in_home=True
        ).order_by('-created')[:4]

    def entradas_recientes(self):
        # devuelve las ultimas 6 entradas
        return self.filter(
            public=True,
        ).order_by('-created')[:6]

    def buscar(self, kword, categoria):
        # devuelve una lista de entradas segun unas palabras clave o categoria
        if categoria:
            return self.filter(
                Q(title__icontains = kword) | Q(resume__icontains = kword),
                category__short_name = categoria,
                public = True,
            ).order_by('-created')
        
        return self.filter(
                Q(title__icontains = kword) | Q(resume__icontains = kword)
            ).order_by('-created')