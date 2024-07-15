from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('', HomePageView.as_view(), name="home"),
    path('about-us',AboutPageView.as_view(), name="about"),
    path('contact-us',contactPageView.as_view(), name="contact"),
    
]