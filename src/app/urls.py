from django.urls import path

from .views import(
    home,
    search_page,
    home_searcher,
    post_ask_home,
)

urlpatterns = [
    path('', home, name="welcome"),
    path('chercher-une-maison', search_page, name="home-search"),
    path('chercheur', home_searcher, name="home-searcher"),
    path('post-data-ask-home', post_ask_home, name="post-ask-home"),
]

