from django.urls import path

from .views import(
    home,
    search_page,
    home_searcher,
    post_ask_home,
    owner_page,
)

urlpatterns = [
    path('', home, name="welcome"),
    path('chercher-une-maison', search_page, name="home-search"),
    path('chercheur', home_searcher, name="home-searcher"),
    path('post-data-ask-home', post_ask_home, name="post-ask-home"),
    path('proprietaire', owner_page, name="owner-page"),
]

