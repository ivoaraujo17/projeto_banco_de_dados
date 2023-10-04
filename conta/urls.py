from django.urls import path
from django.urls.conf import include

app_name = 'conta_bancaria'

urlpatterns = [
    path('criar_conta_bancaria/', name='criar_conta_bancaria')
]