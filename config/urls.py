from django.contrib import admin
from django.urls import path
from todo import views as todo_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', todo_views.index, name='index'),
    path('<int:task_id>/', todo_views.detail, name='detail'),
    path('<int:task_id>/update/', todo_views.update, name='update'),
    path('delete/<int:task_id>/', todo_views.delete, name='delete'),
    path('complete/<int:task_id>/', todo_views.complete_task, name='complete_task'),
]
