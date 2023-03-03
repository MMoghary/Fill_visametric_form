from django.urls import path
from .views import home , fill_form


app_name = 'fill'
urlpatterns = [
    path('', home, name='home'),
    path('fill/', fill_form, name='fill_form')
    ]


