from django.contrib import admin
from django.urls import path, include
from rest_framework.documentation import include_docs_urls

from rest_framework import routers
from todo import views

router = routers.DefaultRouter()
router.register(r'todos', views.TodoView, 'todo')

urlpatterns = [
    path('api/v1/', include(router.urls)),
    path('docs/', include_docs_urls(title='Todo API')),
]


# GET       /api/v1/todos       Get all tasks
# POST      /api/v1/todos       Insert new task
# GET       /api/v1/todos/:id   Get single task
# PUT       /api/v1/todos/:id   Update specific task
# DELETE    /api/v1/todos/:id   Delete task
