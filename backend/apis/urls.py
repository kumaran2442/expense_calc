from django.urls import path
from . import views

3 # name your url patterns here
urlpatterns = [
    path('expenses/', views.getExpenses),
    path('add/expense/',views.createExpense),
    path('delete/expense/<int:pk>',views.deleteExpense),
    path('filter/expense/<str:category>',views.filterCategory),
]
