from django.urls import path
from uni_app import views

app_name = "main" # uni_app NAME ON URLS
urlpatterns = [
    path('test/', views.testView, name='test'),

    path('', views.home_view, name='home'), # home URL USES home_view
    path('<str:type><int:id>/', views.filter_view, name='filter'), # filter URL USES !!! UNUSED !!!
    # RECEIVES type & id TO FILTER
    path('carrera/<int:id>/', views.carrera_view, name='carrera'),# filter URL USES carrera.id
    path('universidad/<int:id>/', views.uni_view, name='uni'),# filter URL USES uni.id
    path('search/', views.search_view, name='search'),# search by forms
    path('unis/', views.unis_view, name='unis'),
    path('compare/<str:type>/', views.compare_view, name='compare')
]