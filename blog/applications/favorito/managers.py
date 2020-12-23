from django.db import models

class FavoritesManager(models.Manager):
    """ Managers del modelo Favorites """

    def entradas_user(self, user):
        """ Metodo que obtiene las entradas favoritas de un usuario """
        return self.filter(
            entry__public = True,
            user = user
        ).order_by('created')
    
    def is_exist_favorite(self, user, entry):
        """ Metodo que devuelve un booleano si el usuario ya tiene una entrada en sus favoritos """
        return self.filter(
            user = user,
            entry = entry
        ).exists()
    

