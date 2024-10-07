from django.urls import path
from uni_app.views import testView, home_view, filter_view

app_name = "main" # uni_app NAME ON URLS
urlpatterns = [
    path('test/', testView, name='test'),
    path('', home_view, name='home'), # home URL USES home_view
    path('<str:type><int:id>/', filter_view, name='filter') # filter URL USES filter_view
] # RECEIVES type & id TO FILTER