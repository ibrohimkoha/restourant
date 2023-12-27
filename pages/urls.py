from django.urls import path
from pages.views import home, message, reservation

app_name = 'pages'
urlpatterns = [
    path('', home , name='home'),
    path('message/', message, name='message'),
    path('reservation/', reservation, name='reservation'),
]