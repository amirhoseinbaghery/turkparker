from django.urls import path

from content.views import about, contactus

app_name = 'content'

urlpatterns = [
    path('about/', about, name='about'),
    path('contactus/', contactus, name='contactus'),

]
