
from django.urls import path

from . import views

urlpatterns = [
    path('',views.index,name="todo"),
    path('todo/',views.index,name="todo"),
    path('addTodo/',views.addTodo, name="addTodo"),
    path('deleteTodo/<int:todo_id>/', views.deleteTodo),
]