from django.urls import path
from .views import contact_us, contact_submit

app_name = 'business'

urlpatterns = [
    path('contact/', contact_us, name='contact_us'),
    path('contact-submit/', contact_submit, name='contact_submit'),
]