from django.urls import path
from . import views

urlpatterns = [
    path('', views.l1_list, name='l1_list'),
    path('l1name/<int:pk>/', views.issue_list, name='issue_list'),
    path('post/new/', views.post_new, name='post_new'),
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
]