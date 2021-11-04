from django.urls import path
from .views import *

urlpatterns = [
    path('catalog/', user_cards),
    path('opinions/', for_companies)
]
