from django.urls import path
from .views import (
    post_agence,
    post_searcher,
    post_owner,
    post_newsletter,
    post_reservation,
    contact_us
)

urlpatterns = [
    path('agence/', post_agence, name="post-agence"),
    path('searcher/', post_searcher, name="post-searcher"),
    path('owner/', post_owner, name="post-owner"),
    path('newsletter/', post_newsletter, name="post-news"),
    path('reservation/', post_reservation, name="post-reservation"),
    path('contact-us/', contact_us, name="contact-us"),

]
