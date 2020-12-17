from django.db import models

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