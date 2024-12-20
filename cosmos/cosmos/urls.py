"""
URL configuration for cosmos project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
#from django.conf.urls import handler404, handler500, handler403, handler400
from django.conf import settings
from cosmos.extra import *

urlpatterns = [
    path('admin/', admin.site.urls), path('git/', git, name="git"),
    path('us/', include('contact_app.urls')),
    path('auth/', include('auth_app.urls')),
    path('blog/', include('blog_app.urls')),
    path('.../', extra, name="extra"),
    path('', include('uni_app.urls')), # REGISTER uni_app.urls BY PATH '' (i.g., ROOT)
] # THIS REMOVED FOR PROD + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


#Error handers
#handler500 = custom_500_view; handler404 = custom_404_view; handler403 = custom_403_view; handler400 = custom_400_view
