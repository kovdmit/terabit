from django.urls import path

from .views import pay

app_name = 'shop'

urlpatterns = [
    path('pay/<int:pk>/', pay, name='pay')
]
