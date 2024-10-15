from django.urls import path
from auth_app.views import View_signin, logout_view, View_login

app_name = "auth" # uni_app NAME ON URLS
urlpatterns = [
    path('signin/', View_signin.as_view(), name='signin'),
    path('logout/', logout_view, name='logout'),
    path('login/', View_login.as_view(), name='login'),
    path('user/', View_signin.as_view(), name='profile')
]