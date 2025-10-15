from django.urls import path
from .views import (
    home,
    search_page,
    home_searcher,
    owner_page,
    home_detail,
    catalogue,
    about,
    agence,
    condition_generale,
    data_caract,
    data_local,
    contact,
)

urlpatterns = [
    path("", home, name="welcome"),
    path("chercher-une-maison", search_page, name="home-search"),
    path("chercheur", home_searcher, name="home-searcher"),
    path("proprietaire", owner_page, name="owner-page"),
    path("catalogue/propriete-<int:id>", home_detail, name="home-detail"),
    path("propriete-<int:id>", home_detail, name="home-detail-index"),
    path("catalogue", catalogue, name="catalogue"),
    path("a-propos", about, name="about"),
    path("contact", contact, name="contact"),
    path("agence-immobiliere", agence, name="agence"),
    path(
        "condition-generale-utilisation",
        condition_generale,
        name="condition-generale-utilisation",
    ),
    path("data/caract", data_caract, name="data"),
    path("data/local", data_local, name="data-local"),
]
