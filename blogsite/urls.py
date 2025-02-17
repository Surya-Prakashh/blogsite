"""blogsite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.urls import path,include
import login.views
import regforms.views
import quotes.views
import quotesform.views
import UserProfile.views
import about.views

from django.conf import settings
from django.conf.urls.static import static
from . import  settings
from django.contrib.staticfiles.urls import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from quotes.views import QuotesView 
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include("home.urls")),
    path('',include("UserProfile.urls")),
    # path('about/',include("about.urls")),
    path('login/',login.views.loginview),
    path('signup/',regforms.views.signup),
    path('quotesform/',quotesform.views.quotesformview),
    path('UserProfile/',UserProfile.views.userview.as_view()),
    path('about/', about.views.aboutview.as_view()),
    path('', include("home.urls")),
    path('quotes/', QuotesView.as_view(), name='quotes'),


]
if settings.DEBUG: # new
    urlpatterns += staticfiles_urlpatterns()
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
