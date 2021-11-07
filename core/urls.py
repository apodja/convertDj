from django.urls import path
from core.views import convert, index
urlpatterns = [
    path('',index, name='home'),
    path('convert/', convert, name='convert')
]
