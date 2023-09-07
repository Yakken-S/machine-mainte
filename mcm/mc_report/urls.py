from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.l1_list, name='l1_list'),
    path('<int:pk>/', views.issue_list, name='issue_list'),
    path('post', views.post_issue, name='post_issue'),
    path('update/<int:pk>/', views.update_issue, name='update_issue'),
    path('delete/<int:pk>', views.delete_issue, name='delete_issue'),
]

