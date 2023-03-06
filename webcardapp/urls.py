from django.urls import path
from webcardapp import views

urlpatterns=[
    path('',views.index)
]