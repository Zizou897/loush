from django.urls import path
from .views import(
    home,
    search_page,
    home_searcher,
    owner_page,
    home_detail,
    catalogue,
    about,
    agence,
    condition_generale
)

urlpatterns = [
    path('', home, name="welcome"),
    path('chercher-une-maison', search_page, name="home-search"),
    path('chercheur', home_searcher, name="home-searcher"),
    path('proprietaire', owner_page, name="owner-page"),
    path('catalogue/<int:id>', home_detail, name="home-detail"),
    path('catalogue', catalogue, name="catalogue"),
    path('a-propos', about, name="about"),
    path('agence-immobiliere', agence, name="agence"),
    path('condition-generale-utilisation', condition_generale, name="condition-generale-utilisation"),
]

