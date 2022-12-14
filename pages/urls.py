from django.urls import path
from .views import HomePagesView, ContactView, AboutView, ServiceView

app_name = 'pages'

urlpatterns = [
    path('', HomePagesView.as_view(), name='home'),
    path('contact/', ContactView.as_view(), name='contact'),
    path('about/', AboutView.as_view(), name='about'),
    path('service/', ServiceView.as_view(), name='service'),
]
