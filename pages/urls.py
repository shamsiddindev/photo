from django.urls import path
from .views import HomePagesView, ContactView

app_name = 'pages'

urlpatterns = [
    path('', HomePagesView.as_view(), name='home'),
    path('contact/', ContactView.as_view(), name='contact'),
]
