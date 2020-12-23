#
from django.urls import path
from . import views

app_name = "favorite_app"

urlpatterns = [
    path(
        'favoritos', 
        views.UserPageListView.as_view(),
        name='favoritos',
    ),  
    path(
        'add-favoritos/<pk>/', 
        views.AddFavoriteView.as_view(),
        name='add_favorito',
    ), 
    path(
        'delete-favoritos/<pk>/', 
        views.DeleteFavoriteView.as_view(),
        name='delete_favorito',
    ),  
]