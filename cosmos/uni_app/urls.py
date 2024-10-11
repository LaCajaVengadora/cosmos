from django.urls import path
from uni_app.views import testView, home_view, filter_view, carrera_view, search_view, uni_view

app_name = "main" # uni_app NAME ON URLS
urlpatterns = [
    path('test/', testView, name='test'),
    path('', home_view, name='home'), # home URL USES home_view
    path('<str:type><int:id>/', filter_view, name='filter'), # filter URL USES !!! UNUSED !!!
    # RECEIVES type & id TO FILTER
    path('carrera/<int:id>/', carrera_view, name='carrera'),# filter URL USES carrera_view
    path('universidad/<int:id>/', uni_view, name='uni'),# filter URL USES carrera_view
    path('search/', search_view, name='search')
]