from django.urls import path
from uni_app.views import testView, home_view, search_view

app_name = "main"
urlpatterns = [
    path('test/', testView, name='test'),
    path('', home_view, name='home'),
    path('<str:type><int:id>', search_view, name='search')
]