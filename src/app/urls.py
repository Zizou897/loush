from django.urls import path

from .views import(
    home,
    search_page,
    home_searcher,
)

urlpatterns = [
    path('', home, name="welcome"),
    path('chercher-une-maison', search_page, name="home-search"),
    path('chercheur', home_searcher, name="home-searcher")
]

