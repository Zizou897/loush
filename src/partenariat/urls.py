from django.urls import path
from .views import (
    post_agence,
    post_searcher,
    post_owner
)

urlpatterns = [
    path('agence/', post_agence, name="post-agence"),
    path('searcher/', post_searcher, name="post-searcher"),
    path('owner/', post_owner, name="post-owner"),

]
