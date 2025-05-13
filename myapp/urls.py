from django.urls import path
from .import views

urlpatterns = [
    path('',views.form,name='forms'),
    path('addemp',views.addemp,name='addemp'),
    path('show',views.show,name='show'),
    path('edit/<int:id>',views.edit,name='edit'),
    path('delete/<int:id>',views.delete,name='delete'),
]