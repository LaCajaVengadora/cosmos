from django.urls import path
from contact_app import views
app_name = "contact" # uni_app NAME ON URLS
urlpatterns = [
    path('', views.usView, name='us'),
]