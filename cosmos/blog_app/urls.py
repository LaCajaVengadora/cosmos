from django.urls import path
from blog_app.views import blog_view, make_view

app_name = "blog" # uni_app NAME ON URLS
urlpatterns = [
    path('', blog_view , name="view"),
    path('make/', make_view , name="make"),
]